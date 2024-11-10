from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .forms import LoginForm

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']

            # Autenticar al usuario usando el backend personalizado
            user = authenticate(request, dni=dni, fecha_nacimiento=fecha_nacimiento)

            if user is not None:
                # Si el usuario es autenticado, hacer login y redirigir a /reservas
                auth_login(request, user)
                return redirect('/')
            else:
                # Si no se encuentra el usuario, mostrar un mensaje de error
                messages.error(request, "Credenciales inválidas. Inténtalo de nuevo.")
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al login después de cerrar sesión