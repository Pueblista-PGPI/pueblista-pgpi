from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from gestion_reservas.models import Reserva
from django.shortcuts import get_object_or_404
from django.contrib import messages

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