from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('dni', 'nombre', 'apellidos', 'telefono',
                    'tipo_usuario', 'is_staff', 'is_active')
    list_filter = ('tipo_usuario', 'is_staff', 'is_active')
    search_fields = ('dni', 'nombre', 'apellidos', 'telefono')
    ordering = ('dni',)

    fieldsets = (
        (None, {'fields': ('dni', 'password')}),
        ('Información Personal', {'fields': ('nombre',
                                             'apellidos', 'fecha_nacimiento',
                                             'telefono', 'direccion_postal',
                                             'tipo_usuario')}),

        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('dni', 'fecha_nacimiento', 'nombre', 'apellidos',
                       'telefono', 'direccion_postal', 'password1',
                       'password2', 'tipo_usuario', 'is_staff', 'is_active'),
        }),
    )

    filter_horizontal = ('groups', 'user_permissions',)


# Registrar el modelo en el admin de Django
admin.site.register(CustomUser, CustomUserAdmin)
