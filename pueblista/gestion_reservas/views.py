from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Reserva
from gestion_espacios.models import EspacioPublico
from datetime import datetime
from django.contrib.sessions.models import Session


@login_required
def calendario_reservas(request, id):
    # Obtener todas las reservas para la fecha seleccionada o para hoy por defecto
    fecha_seleccionada = request.GET.get('fecha') if request.GET.get('fecha') else request.session.get('fecha')
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
    })

@login_required
def crear_reserva(request, id):
    if request.method == 'POST':
        espacio = get_object_or_404(EspacioPublico, id=id)
        fecha = request.POST.get('fecha')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fin = request.POST.get('hora_fin')
        request.session['fecha'] = fecha
        
        # Validar si ya existe una reserva en este intervalo
        if Reserva.objects.filter(
            espacio=espacio,
            fecha=fecha,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin
        ).exists():
            return redirect('calendario_reservas', id=espacio.id)  # Manejo de conflicto
        
        # Crear la reserva
        Reserva.objects.create(
            espacio=espacio,
            usuario=request.user,
            fecha=fecha,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin
        )
        
        return redirect('calendario_reservas', id=espacio.id)
