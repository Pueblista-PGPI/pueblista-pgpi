from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail.backends.smtp import EmailBackend
from django.contrib import messages
import os
from gestion_notificaciones.models import Notificacion
from home.models import AyuntamientoInfo


def send_email(request, subject, full_message, success_message):
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
            subject=subject,
            message=full_message,
            from_email=email_host_user,
            recipient_list=[contact_email],
            fail_silently=False,
            connection=email_backend,
        )

        messages.success(request, success_message)

    except Exception:
        # Mostrar un mensaje de error
        messages.error(request, 'Ocurrió un error al enviar el mensaje')


# Create your views here.
@login_required
def home(request):
    ayuntamiento_info = AyuntamientoInfo.objects.all()

    texto_pueblista = """ Pueblista es un equipo de cinco estudiantes de
    Ingeniería Informática de Sevilla. Apasionados por la vida en los pueblos, trabajamos para mejorar la vida rural mediante herramientas tecnológicas que fomenten el desarrollo y la conexión entre comunidades.\n Gracias a Pueblista,  podrás disfrutar de tu pueblo como nunca antes."""

    user = request.user

    notificaciones_no_leidas_count = Notificacion.objects.filter(usuario=user, leida=False).count()

    if request.method == 'POST':
        if 'message' in request.POST:  # Comprobar si el formulario envió un mensaje de contacto
            message = request.POST.get('message')

            # Obtener los datos del usuario autenticado
            user_nombre = request.user.nombre
            user_apellidos = request.user.apellidos
            user_dni = request.user.dni
            user_telefono = request.user.telefono

            # Construir el cuerpo del mensaje
            full_message = f"""De: {user_nombre + " " + user_apellidos}
            (DNI: {user_dni}, Teléfono: {user_telefono})\n\nMensaje:\n{message}"""


            send_email(request, 'Mensaje de contacto desde Pueblista', full_message, 'Muchas gracias por tu ayuda.')



    return render(request, 'home.html', {
        'ayuntamiento_info': ayuntamiento_info,
        "pueblista": texto_pueblista,
        "contact_text": 'Contacta con nosotros!',
        "user": user,
        "notificaciones": notificaciones_no_leidas_count
    })


@login_required
def edit_ayuntamiento_info(request, id):
    info = get_object_or_404(AyuntamientoInfo, id=id)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        info.titulo = titulo
        info.descripcion = descripcion
        info.save()
        messages.success(request, 'Información actualizada con éxito.')
        return redirect('home')
    return render(request, 'home.html', {'ayuntamiento_info': AyuntamientoInfo.objects.all()})


@login_required
def add_ayuntamiento_info(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        AyuntamientoInfo.objects.create(titulo=titulo, descripcion=descripcion)
        messages.success(request, 'Nueva información añadida con éxito.')
        return redirect('home')
    return render(request, 'home.html', {'ayuntamiento_info': AyuntamientoInfo.objects.all()})
