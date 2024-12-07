from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notificacion

@login_required
def mis_notificaciones(request):
    # Filtramos las notificaciones del usuario autenticado
    notificaciones = Notificacion.objects.filter(usuario=request.user).order_by('-fecha')
    # Pasamos los datos al contexto
    return render(request, 'notificaciones.html', {'notificaciones': notificaciones})

@login_required
def marcar_leida(request, notificacion_id):
    # Obtenemos la notificación y verificamos que pertenezca al usuario autenticado
    notificacion = get_object_or_404(Notificacion, id=notificacion_id, usuario=request.user)
    notificacion.leida = True
    notificacion.save()
    return redirect('notificaciones')

def borrar_notificacion(request, notificacion_id):
    # Obtenemos la notificación y verificamos que pertenezca al usuario autenticado
    notificacion = get_object_or_404(Notificacion, id=notificacion_id, usuario=request.user)
    notificacion.delete()
    return redirect('notificaciones')

def borrar_todas_leidas(request):
    # Obtenemos todas las notificaciones no leídas del usuario autenticado
    notificaciones = Notificacion.objects.filter(usuario=request.user, leida=True)
    # Borramos todas las notificaciones
    notificaciones.delete()
    return redirect('notificaciones')
