from gestion_notificaciones.models import Notificacion

def notificaciones(request):
    if request.user.is_authenticated:
        notificaciones_no_leidas = Notificacion.objects.filter(usuario=request.user, leida=False).count()
    else:
        notificaciones_no_leidas = 0
    return {'notificaciones': notificaciones_no_leidas}