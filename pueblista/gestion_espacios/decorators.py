from django.http import HttpResponseForbidden
from functools import wraps


# Decorador para verificar el tipo de usuario antes de permitir
# el acceso a la vista
def tipo_usuario_requerido(*tipos_usuario):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.tipo_usuario in tipos_usuario:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden('No tienes permiso para acceder a esta vista.')
        return _wrapped_view
    return decorator
