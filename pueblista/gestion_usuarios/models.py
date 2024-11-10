# Paso 1: Crear el Custom User Model y el Manager Personalizado

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.crypto import get_random_string
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, dni, nombre, apellidos, telefono, direccion_postal, fecha_nacimiento, password=None, **extra_fields):
        if not dni:
            raise ValueError('El DNI es obligatorio')
        if not fecha_nacimiento:
            raise ValueError('La fecha de nacimiento es obligatoria')
        if not nombre:
            raise ValueError('El nombre es obligatorio')
        if not apellidos:
            raise ValueError('Los apellidos son obligatorios')
        if not telefono:
            raise ValueError('El teléfono es obligatorio')
        if not direccion_postal:
            raise ValueError('La dirección postal es obligatoria')

        if password is None:
            # Genera una contraseña aleatoria que será cifrada, pero que no se usará realmente
            password = get_random_string(length=16)

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        user = self.model(
            dni=dni,
            fecha_nacimiento=fecha_nacimiento,
            nombre=nombre,
            apellidos=apellidos,
            telefono=telefono,
            direccion_postal=direccion_postal,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, dni, nombre, apellidos, telefono, direccion_postal, fecha_nacimiento, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('tipo_usuario', CustomUser.SUPERUSUARIO)

        return self.create_user(
            dni=dni,
            nombre=nombre,
            apellidos=apellidos,
            telefono=telefono,
            direccion_postal=direccion_postal,
            fecha_nacimiento=fecha_nacimiento,
            password=password,
            **extra_fields
        )



class CustomUser(AbstractBaseUser, PermissionsMixin):
    USUARIO_FINAL = 'usuario_final'
    PERSONAL_ADMINISTRATIVO = 'personal_administrativo'
    SUPERUSUARIO = 'superusuario'

    TIPOS_USUARIO = [
        (USUARIO_FINAL, 'Usuario Final'),
        (PERSONAL_ADMINISTRATIVO, 'Personal Administrativo'),
        (SUPERUSUARIO, 'Superusuario'),
    ]

    dni = models.CharField(max_length=9)
    fecha_nacimiento = models.DateField()
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion_postal = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=30, choices=TIPOS_USUARIO, default=USUARIO_FINAL)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Define si el usuario tiene acceso a partes administrativas (no /admin)
    is_superuser = models.BooleanField(default=False)  # Define si el usuario es superusuario y tiene acceso completo a /admin

    objects = CustomUserManager()

    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = ['fecha_nacimiento', 'nombre', 'apellidos', 'telefono', 'direccion_postal']

    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.tipo_usuario})"
    
