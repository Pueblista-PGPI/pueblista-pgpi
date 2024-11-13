from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import CustomUser
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .decorators import tipo_usuario_requerido

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
    return render(request, 'user_list.html', {'users': users})
