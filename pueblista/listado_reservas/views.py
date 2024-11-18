from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gestion_reservas.models import Reserva

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
            'fecha': reserva.fecha,
            'hora_inicio': reserva.hora_inicio,
            'hora_fin': reserva.hora_fin,
            'estado': reserva.estado,
            'espacio': reserva.espacio.nombre
        }
        for reserva in reservas
    ]

    return render(request, 'listado_reservas.html', {"reservas": reservas, "query": query})