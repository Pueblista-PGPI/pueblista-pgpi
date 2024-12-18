from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


from gestion_notificaciones.models import Notificacion
from gestion_reservas.models import SolicitudReservaEspecial

from .models import CustomUser
from .forms import LoginForm
from .decorators import tipo_usuario_requerido

from django.http import JsonResponse
from gestion_reservas.models import Reserva

@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']

            # Autenticar al usuario usando el backend personalizado
            user = authenticate(request, dni=dni,
                                fecha_nacimiento=fecha_nacimiento)

            if user is not None:
                # Si el usuario es autenticado, hacer login
                # y redirigir a /reservas
                auth_login(request, user)
                return redirect('/')
            else:
                # Si no se encuentra el usuario, mostrar un mensaje de error
                messages.error(
                    request, "Credenciales inválidas. Inténtalo de nuevo."
                )
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al login después de cerrar sesión


@login_required  # Asegura que solo los usuarios autenticados puedan acceder a esta vista
def perfil(request):
    # Accedemos al usuario actual a través del objeto request.user
    usuario = request.user
    # Pasamos el objeto usuario al template
    return render(request, 'perfil.html', {'usuario': usuario})


@login_required
@tipo_usuario_requerido('superusuario', 'personal_administrativo')
def user_list(request):
    users = CustomUser.objects.all()
    users = users.exclude(tipo_usuario='superusuario')
    return render(request, 'user_list.html', {'users': users})


@login_required
def eliminar_reservas_y_cerrar_sesion(request):
    if request.method == 'POST':
        usuario = request.user
        # Eliminar todas las reservas del usuario
        Reserva.objects.filter(usuario=usuario).delete()
        Notificacion.objects.filter(usuario=usuario).delete()
        SolicitudReservaEspecial.objects.filter(usuario=usuario).delete()
        # Cerrar sesión
        logout(request)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})