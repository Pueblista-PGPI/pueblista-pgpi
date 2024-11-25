from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from gestion_reservas.models import Reserva
from django.shortcuts import get_object_or_404
from django.contrib import messages
from datetime import datetime
from gestion_sms.sms import send_sms
from gestion_notificaciones.models import Notificacion


@login_required
def listado_reservas(request):
    usuario = request.user
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if fecha_inicio and fecha_fin:
        reservas = Reserva.objects.filter(
            usuario=usuario,
            fecha__range=[fecha_inicio, fecha_fin],
            estado='Realizada'
        ).exclude(nombre='LIMPIEZA').order_by('fecha')
    else:
        reservas = Reserva.objects.filter(
            usuario=usuario,
            estado='Realizada'
        ).exclude(nombre='LIMPIEZA').order_by('fecha')

    reservas = [
        {
            'id': reserva.id,
            'fecha': reserva.fecha,
            'hora_inicio': reserva.hora_inicio,
            'hora_fin': reserva.hora_fin,
            'estado': reserva.estado,
            'espacio': reserva.espacio.nombre,
            'subespacio': reserva.subespacio if reserva.subespacio != "No procede" else None,
            'especial': reserva.espacio.espacio_especial,
        }
        for reserva in reservas
    ]

    return render(request, 'listado_reservas.html', {
        "reservas": reservas,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin
    })

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
def modificar_estado(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    espacio_id = reserva.espacio.id
    if request.method == 'POST':
        estado = request.POST.get('estado')
        reserva.estado = estado
        reserva.save()

        if estado == 'Cancelada':
            notificacion = Notificacion(mensaje=f"Su reserva del espacio {reserva.espacio.nombre} para el día {reserva.fecha} y la hora {reserva.hora_inicio} ha sido cancelada.", usuario=reserva.usuario)
            notificacion.save()
            reserva.delete()
        messages.success(request, "El estado de la reserva se ha modificado exitosamente.")
        return redirect(f'/espacios/reservas_fecha/{espacio_id}/')
    return render(request, 'modificar_estado.html', {'reserva': reserva})
