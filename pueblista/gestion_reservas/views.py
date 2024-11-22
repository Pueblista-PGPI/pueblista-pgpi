from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from gestion_usuarios.decorators import tipo_usuario_requerido

from .forms import SolicitudReservaEspecialForm
from .models import Reserva
from gestion_espacios.models import EspacioPublico
from datetime import datetime, timedelta
from django.contrib import messages
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from gestion_espacios.models import EspacioPublico
from .models import SolicitudReservaEspecial
from datetime import datetime


def comprueba_horas(hora_inicio, hora_fin):
    if hora_inicio >= hora_fin:
        return True
    return False

@login_required
def solicitud_reserva_especial(request, id):
    espacio = get_object_or_404(EspacioPublico, id=id)

    # Obtener la fecha seleccionada desde la sesión
    fecha_seleccionada = request.session.get('fecha')
    peticiones_por_usuario_en_espacio_en_fecha = SolicitudReservaEspecial.objects.filter(usuario=request.user, espacio=espacio, fecha=fecha_seleccionada, estado='PENDIENTE').count()
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
def aceptar_solicitud(request, id):
    if request.method == 'POST':
        solicitud_id = request.POST.get('solicitud_id')
        solicitud = get_object_or_404(SolicitudReservaEspecial, id=solicitud_id)
        nombre_reserva = request.POST.get('nombre_reserva')
        
        Reserva.objects.create(
            fecha=solicitud.fecha,
            hora_inicio=solicitud.hora_inicio,
            hora_fin=solicitud.hora_fin,
            estado=Reserva.REALIZADA,
            espacio=solicitud.espacio,
            usuario=request.user,
            nombre=nombre_reserva
        )
        
        solicitud.estado = 'ACEPTADA'
        solicitud.save()
        
        if solicitud.espacio.limpieza:
            # crear dos reservas con nombre LIMPIEZA que ocupen todo el día y que esté en estado REALIZADA mismamente, lo único que me importa es que haya dos,
            # una para el día previo a la reserva y otra para el día posterior a la reserva
            
            # Reserva para el día previo
            Reserva.objects.create(
                fecha=solicitud.fecha - timedelta(days=1),
                hora_inicio=datetime.min.time(),
                hora_fin=datetime.max.time(),
                estado=Reserva.REALIZADA,
                espacio=solicitud.espacio,
                usuario=request.user,
                nombre='LIMPIEZA'
            )
            
            # Reserva para el día posterior
            Reserva.objects.create(
                fecha=solicitud.fecha + timedelta(days=1),
                hora_inicio=datetime.min.time(),
                hora_fin=datetime.max.time(),
                estado=Reserva.REALIZADA,
                espacio=solicitud.espacio,
                usuario=request.user,
                nombre='LIMPIEZA'
            )
            
            
        # ahora lo que hay que hacer es, si el espacio en el que se ha reservao se llama "Salón de Reuniones", entonces
        # cojo todas las reservas que haya entre esas horas y en esa fecha y las cancelo, NO LAS BORRO, las cancelo estado.CANCELADA
        # pero cojo solo las reservas de la Biblioteca
        # todas las reservas contenidas en ese intervalo de tiempo... no sé si se está haciendo
        
        if solicitud.espacio.nombre == 'Salón de Reuniones':
            # Obtener todas las reservas para la fecha y intervalo de horas de solicitud
            reservas_a_cancelar = Reserva.objects.filter(
                Q(espacio__nombre='Biblioteca'),
                Q(fecha=solicitud.fecha),
                Q(hora_inicio__lt=solicitud.hora_fin),
                Q(hora_fin__gt=solicitud.hora_inicio)
    )
            
            # Cancelar todas las reservas
            for reserva in reservas_a_cancelar:
                print(reserva)
                reserva.delete()
                
        messages.success(request, 'La solicitud ha sido aceptada con éxito.')
        return redirect('solicitudes_pendientes', id=solicitud.espacio.id)

    return redirect('solicitudes_pendientes', id=solicitud.espacio.id)
    

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
        'reservas': reservas
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
            if comprueba_horas(hora_inicio, hora_fin):
                messages.error(request, "La hora de inicio debe ser menor a la hora de fin.")
                return redirect('calendario_reservas', id=espacio.id)
            request.session['fecha'] = fecha
            
            if espacio.nombre == 'Biblioteca':
                # validar si en el salón de reuniones hay una reserva en ese intervalo
                reservas = Reserva.objects.filter(
                    espacio__nombre='Salón de Reuniones',
                    fecha=fecha,
                    hora_inicio__lt=hora_fin,
                    hora_fin__gt=hora_inicio
                )
                if reservas.exists():
                    messages.error(request, "Ya existe una reserva en el Salón de Reuniones en este intervalo.")
                    return redirect('calendario_reservas', id=espacio.id)
                
            numero_de_reservas_por_usuario_en_espacio_en_fecha = Reserva.objects.filter(usuario=request.user, espacio=espacio, fecha=fecha).count()
            
            if numero_de_reservas_por_usuario_en_espacio_en_fecha >= 4:
                messages.error(request, "Ya has realizado 4 reservas en este espacio para esta fecha.")
                return redirect('calendario_reservas', id=espacio.id)

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
                # request.session.pop('fecha', None)
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