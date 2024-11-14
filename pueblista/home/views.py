from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail.backends.smtp import EmailBackend
from django.contrib import messages
import os

from gestion_usuarios.decorators import tipo_usuario_requerido
from home.models import Configuracion


# Create your views here.
@login_required
def home(request):
    config, created = Configuracion.objects.get_or_create(id=1)
    texto_ayuntamiento = config.texto_ayuntamiento
    
    texto_pueblista = """ Pueblista es un equipo de cinco estudiantes de
    Ingeniería Informática de Sevilla. Apasionados por la vida en los pueblos,
    trabajamos para mejorar la vida rural mediante herramientas tecnológicas
    que fomenten el desarrollo y la conexión entre comunidades.\n Gracias
    Pueblista,  podrás disfrutar de tu pueblo como nunca antes."""
    
    user = request.user

    if request.method == 'POST':
        if 'nuevo_ayuntamiento' in request.POST:  # Comprobar si el formulario envió un cambio de texto
            texto_ayuntamiento = request.POST.get('nuevo_ayuntamiento', '').strip()
            config.texto_ayuntamiento = texto_ayuntamiento
            config.save()
            messages.success(request, 'Texto del ayuntamiento actualizado con éxito.')
            return redirect('home')  # Redirigir para evitar reenvío del formulario

        elif 'message' in request.POST:  # Comprobar si el formulario envió un mensaje de contacto
            message = request.POST.get('message')

            # Obtener los datos del usuario autenticado
            user_nombre = request.user.nombre
            user_apellidos = request.user.apellidos
            user_dni = request.user.dni
            user_telefono = request.user.telefono

            # Construir el cuerpo del mensaje
            full_message = f"""De: {user_nombre + " " + user_apellidos}
            (DNI: {user_dni}, Teléfono: {user_telefono})\n\nMensaje:\n{message}"""

            email_host = os.getenv('EMAIL_HOST')
            email_port = int(os.getenv('EMAIL_PORT', 587))
            email_host_user = os.getenv('EMAIL_HOST_USER')
            # Se usa la contraseña de aplicación de la cuenta de correo
            email_host_password = os.getenv('EMAIL_HOST_PASSWORD')
            email_use_tls = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
            contact_email = os.getenv('CONTACT_EMAIL')

            try:
                email_backend = EmailBackend(
                    host=email_host,
                    port=email_port,
                    username=email_host_user,
                    password=email_host_password,
                    use_tls=email_use_tls
                )

                # Enviar el correo
                send_mail(
                    subject="Mensaje de contacto desde pueblista.com",
                    message=full_message,
                    from_email=email_host_user,
                    recipient_list=[contact_email],
                    fail_silently=False,
                    connection=email_backend,
                )

                # Mostrar un mensaje de éxito
                messages.success(request, 'Muchas gracias por tu ayuda.')

            except Exception:
                # Mostrar un mensaje de error
                messages.error(request, 'Ocurrió un error al enviar el mensaje')

    return render(request, 'home.html', {
        "ayuntamiento": texto_ayuntamiento,
        "pueblista": texto_pueblista,
        "contact_text": 'Contacta con nosotros!',
        "user": user
    })

@login_required
@tipo_usuario_requerido("superusuario")
def editar_ayuntamiento(request):
    return render(request, 'editar_ayuntamiento.html')
