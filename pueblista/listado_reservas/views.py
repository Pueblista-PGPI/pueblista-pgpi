from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from gestion_reservas.models import Reserva
from django.shortcuts import get_object_or_404
from django.contrib import messages
from datetime import datetime


@login_required
def listado_reservas(request):
    usuario = request.user
    query = request.GET.get('q')
    if query:
        reservas = Reserva.objects.filter(usuario=usuario, espacio__nombre__icontains=query).order_by('fecha')
    else:
        reservas = Reserva.objects.filter(usuario=usuario).order_by('fecha')

    reservas = [
        {
            'id': reserva.id,
            'fecha': reserva.fecha,
            'hora_inicio': reserva.hora_inicio,
            'hora_fin': reserva.hora_fin,
            'estado': reserva.estado,
            'espacio': reserva.espacio.nombre
        }
        for reserva in reservas
    ]

    return render(request, 'listado_reservas.html', {"reservas": reservas, "query": query})


@login_required
def eliminar_reserva(request, reserva_id):
    # Intenta obtener la reserva asociada al usuario actual
    if request.user.tipo_usuario == 'personal_administrativo' or request.user.tipo_usuario == 'superusuario':
        reserva = get_object_or_404(Reserva, id=reserva_id)
    else:
        reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)

    try:
        # Elimina la reserva
        reserva.delete()
        # Muestra un mensaje de éxito al usuario
        messages.success(request, "La reserva se ha cancelado exitosamente.")
    except Exception as e:
        # Si ocurre un error, muestra un mensaje de error
        messages.error(request, f"Ocurrió un error al cancelar la reserva: {str(e)}")

    return redirect('listado_reservas')


@login_required
def modificar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
    espacio = reserva.espacio
    fecha = reserva.fecha

    # Obtener todas las reservas en el mismo espacio y fecha
    reservas = Reserva.objects.filter(espacio=espacio, fecha=fecha).exclude(id=reserva_id)

    # Generar lista de horas disponibles
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

    horas_disponibles = []
    for inicio, fin in horarios:
        hora_inicio = datetime.strptime(inicio, "%H:%M").time()
        hora_fin = datetime.strptime(fin, "%H:%M").time()
        if not reservas.filter(hora_inicio__lt=hora_fin, hora_fin__gt=hora_inicio).exists() and (hora_inicio != reserva.hora_inicio or hora_fin != reserva.hora_fin):
            horas_disponibles.append((inicio, fin))

    if request.method == 'POST':
        hora_inicio = request.POST.get('hora_inicio')
        hora_fin = request.POST.get('hora_fin')

        # Verificar que no haya conflictos con otras reservas
        if not reservas.filter(hora_inicio__lt=hora_fin, hora_fin__gt=hora_inicio).exists():
            reserva.hora_inicio = hora_inicio
            reserva.hora_fin = hora_fin
            reserva.save()
            messages.success(request, "La reserva se ha modificado exitosamente.")
        else:
            messages.error(request, "Ya existe una reserva en este intervalo.")
        return redirect('listado_reservas')


@login_required
def modificar_estado(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    espacio_id = reserva.espacio.id
    if request.method == 'POST':
        estado = request.POST.get('estado')
        reserva.estado = estado
        reserva.save()
        messages.success(request, "El estado de la reserva se ha modificado exitosamente.")
        return redirect(f'/espacios/reservas_fecha/{espacio_id}/')
    return render(request, 'modificar_estado.html', {'reserva': reserva})
