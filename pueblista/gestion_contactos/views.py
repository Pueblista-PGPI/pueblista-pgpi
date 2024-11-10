from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail.backends.smtp import EmailBackend
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import os
from dotenv import load_dotenv

# Create your views here.
load_dotenv()

@login_required
def contact_mail(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        
        # Obtener los datos del usuario autenticado
        user_nombre = request.user.nombre
        user_apellidos= request.user.apellidos
        user_dni = request.user.dni
        user_telefono = request.user.telefono

        # Construir el cuerpo del mensaje
        full_message = f"De: {user_nombre +" " + user_apellidos} (DNI: {user_dni}, Teléfono: {user_telefono})\n\nMensaje:\n{message}"

        email_host = os.getenv('EMAIL_HOST')
        email_port = int(os.getenv('EMAIL_PORT', 587))
        email_host_user = os.getenv('EMAIL_HOST_USER')
        email_host_password = os.getenv('EMAIL_HOST_PASSWORD') # Se usa la contraseá de aplicación de la cuenta de correo
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
            messages.success(request, 'Mensaje enviado correctamente, muchas gracias por tu ayuda.')
        
        except Exception as e:
            # Mostrar un mensaje de error
            messages.error(request, 'Ha ocurrido un error al enviar el mensaje. Inténtalo de nuevo.')
                
    return render(request, 'contact_mail.html', {'contact_text': 'Contacta con nosotros!'})

