from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from gestion_usuarios.decorators import tipo_usuario_requerido

from .forms import CancelarSolicitudForm, SolicitudReservaEspecialForm
from .models import Reserva
from gestion_espacios.models import EspacioPublico
from datetime import datetime
from django.contrib.sessions.models import Session
from django.contrib import messages
from home.views import send_email

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from gestion_espacios.models import EspacioPublico
from .models import SolicitudReservaEspecial
from datetime import datetime

@login_required
def solicitud_reserva_especial(request, id):
    espacio = get_object_or_404(EspacioPublico, id=id)

    # Obtener la fecha seleccionada desde la sesión
    fecha_seleccionada = request.session.get('fecha')
    peticiones_por_usuario_en_espacio_en_fecha = SolicitudReservaEspecial.objects.filter(usuario=request.user, espacio=espacio, fecha=fecha_seleccionada).count()
    if peticiones_por_usuario_en_espacio_en_fecha >= 1:
                messages.error(request, 'Ya has solicitado una reserva especial para este espacio en esta fecha.')
                return redirect('calendario_reservas', id=id)
    if request.method == 'POST':
        form = SolicitudReservaEspecialForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.espacio = espacio
            solicitud.usuario = request.user
            solicitud.fecha = fecha_seleccionada  # Asignar la fecha seleccionada
            solicitud.save()
            messages.success(request, 'Tu solicitud de reserva especial ha sido enviada con éxito.')
            request.session.pop('fecha', None)
            return redirect('calendario_reservas', id=id)
    else:
        # Crea el formulario pasando los valores iniciales
        form = SolicitudReservaEspecialForm(initial={
            'espacio': espacio,
            'fecha': fecha_seleccionada,
            'usuario': request.user
        })

    return render(request, 'solicitud_reserva_especial.html', {
        'espacio': espacio,
        'form': form,
        'id': id
    })

@login_required
def mis_solicitudes(request,id):
    espacio = get_object_or_404(EspacioPublico, id=id)
    solicitudes = SolicitudReservaEspecial.objects.filter(usuario=request.user, espacio=espacio)
    return render(request, 'mis_solicitudes.html', {
        'solicitudes': solicitudes,
        'espacio': espacio
    })
    
@login_required
@tipo_usuario_requerido('superusuario', 'personal_administrativo')
def solicitudes_pendientes(request, id):
    espacio = get_object_or_404(EspacioPublico, id=id)
    solicitudes = SolicitudReservaEspecial.objects.filter(espacio=espacio, estado='PENDIENTE')
    
    if request.method == 'POST':
        solicitud_id = request.POST.get('solicitud_id')
        motivo = request.POST.get('motivo')
        solicitud = get_object_or_404(SolicitudReservaEspecial, id=solicitud_id)
        if motivo:
            solicitud.estado = 'cancelada'
            solicitud.motivo_cancelacion = motivo
            solicitud.save()
            messages.success(request, 'La solicitud ha sido cancelada con éxito.')
            return JsonResponse({'success': True})
    
    return render(request, 'solicitudes_pendientes.html', {
        'solicitudes': solicitudes,
        'espacio': espacio
    })

@login_required
@tipo_usuario_requerido('superusuario', 'personal_administrativo')
def cancelar_solicitud(request, solicitud_id,id):
    solicitud = get_object_or_404(SolicitudReservaEspecial, id=solicitud_id)

    if request.method == 'POST':
        form = CancelarSolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            solicitud.estado = 'CANCELADA'
            form.save()
            messages.success(request, 'La solicitud ha sido cancelada con éxito.')
            return redirect('solicitudes_pendientes', id=solicitud.espacio.id)
    else:
        form = CancelarSolicitudForm(instance=solicitud)

    return render(request, 'cancelar_solicitud.html', {
        'form': form,
        'solicitud': solicitud,
    }) 



@login_required
def calendario_reservas(request, id):
    # Obtener todas las reservas para la fecha seleccionada o para hoy por defecto
    fecha_seleccionada = request.GET.get('fecha') if request.GET.get('fecha') else request.session.get('fecha')
    if fecha_seleccionada is None:
        fecha_seleccionada = datetime.now().strftime('%Y-%m-%d')
        
    #añadelo a la sesion
    request.session['fecha'] = fecha_seleccionada

    if fecha_seleccionada < datetime.now().strftime('%Y-%m-%d'):
        request.session.pop('fecha', None)
        messages.error(request, "No se pueden hacer reservas en fechas pasadas.")
        return redirect('calendario_reservas', id=id)
    espacio = get_object_or_404(EspacioPublico, id=id)  # Obtener el espacio con ese ID
    reservas = Reserva.objects.filter(fecha=fecha_seleccionada, espacio=espacio).order_by('hora_inicio')

    # Estructura de horarios
    horarios = [
        ('09:00', '10:00'),
        ('10:00', '11:00'),
        ('11:00', '12:00'),
        ('12:00', '13:00'),
        ('13:00', '14:00'),
        ('16:00', '17:00'),
        ('17:00', '18:00'),
        ('18:00', '19:00'),
        ('19:00', '20:00'),
        ('20:00', '21:00')
    ]

    # Crear un diccionario que asocie cada horario con su reserva (si existe)
    horarios_reservas = []
    for inicio, fin in horarios:
        hora_inicio = datetime.strptime(inicio, "%H:%M").time()
        hora_fin = datetime.strptime(fin, "%H:%M").time()
        reserva = reservas.filter(hora_inicio=hora_inicio, hora_fin=hora_fin).first()
        horarios_reservas.append({
            'hora_inicio': inicio,
            'hora_fin': fin,
            'reserva': reserva,
            'mia': reserva.usuario == request.user if reserva else False
        })

    return render(request, 'calendario_reservas.html', {
        'fecha_seleccionada': fecha_seleccionada,
        'horarios_reservas': horarios_reservas,
        'espacio': espacio,
        'nombre_completo': request.user.nombre + ' ' + request.user.apellidos,
        'reserva_id': -1,
    })


@login_required
def crear_reserva(request, id):
    espacio = '#'
    try:
        espacio = get_object_or_404(EspacioPublico, id=id)
        if request.method == 'POST':
            fecha = request.POST.get('fecha')
            hora_inicio = request.POST.get('hora_inicio')
            hora_fin = request.POST.get('hora_fin')
            request.session['fecha'] = fecha

            # Validar si ya existe una reserva en este intervalo
            if not Reserva.objects.filter(
                espacio=espacio,
                fecha=fecha,
                hora_inicio=hora_inicio,
                hora_fin=hora_fin
            ).exists() and not Reserva.objects.filter(
                fecha=fecha,
                hora_inicio=hora_inicio,
                hora_fin=hora_fin,
                usuario=request.user
            ).exists():
                # Crear la reserva
                Reserva.objects.create(
                    espacio=espacio,
                    usuario=request.user,
                    fecha=fecha,
                    hora_inicio=hora_inicio,
                    hora_fin=hora_fin
                )
                messages.success(request, "La reserva se ha creado exitosamente.")
                request.session.pop('fecha', None)
            else:
                messages.error(request, "Ya existe una reserva en este intervalo.")
        return redirect('calendario_reservas', id=espacio.id) 
    except Exception as e:
        messages.error(request, f"Ocurrió un error al crear la reserva: {str(e)}")
        return redirect('calendario_reservas', id=espacio)


@login_required
def cancelar_reserva(request, id):
    # Intenta obtener la reserva asociada al usuario actual
    reserva = get_object_or_404(Reserva, id=id, usuario=request.user)
    espacio_id = reserva.espacio.id

    try:
        # Elimina la reserva
        reserva.delete()
        # Muestra un mensaje de éxito al usuario
        messages.success(request, "La reserva se ha cancelado exitosamente.")
    except Exception as e:
        # Si ocurre un error, muestra un mensaje de error
        messages.error(request, f"Ocurrió un error al cancelar la reserva: {str(e)}")

    return redirect('calendario_reservas', id=espacio_id)

    # Redirige al calendario de reservas