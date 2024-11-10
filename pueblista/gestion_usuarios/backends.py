from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class DNIFechaNacimientoBackend(BaseBackend):
    def authenticate(self, request, dni=None, fecha_nacimiento=None, tipo_usuario=None, **kwargs):
        User = get_user_model()
        try:
            if tipo_usuario:
                # Buscar usuario por DNI, fecha de nacimiento y tipo de usuario
                user = User.objects.get(dni=dni, fecha_nacimiento=fecha_nacimiento, tipo_usuario=tipo_usuario)
            else:
                # Si no se especifica tipo_usuario, buscar solo por DNI y fecha de nacimiento
                user = User.objects.get(dni=dni, fecha_nacimiento=fecha_nacimiento)

            if user is not None and user.is_active:
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

        