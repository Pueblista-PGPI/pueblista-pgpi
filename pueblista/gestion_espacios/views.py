import base64
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from gestion_usuarios.decorators import tipo_usuario_requerido
from .models import EspacioPublico
from .forms import EspacioPublicoForm
from gestion_reservas.models import Reserva


@login_required
@tipo_usuario_requerido('superusuario', 'personal_administrativo')
def edit(request, id):
    espacio = get_object_or_404(EspacioPublico, id=id)
    foto_original = espacio.fotos  # Guarda la foto original antes de procesar el formulario

    if request.method == 'POST':
        form = EspacioPublicoForm(request.POST, request.FILES, instance=espacio)
        if form.is_valid():
            espacio = form.save(commit=False)

            # Si se sube una nueva foto, actualízala; de lo contrario, conserva la anterior
            if 'fotos' in request.FILES:
                foto = request.FILES['fotos'].read()
                espacio.fotos = base64.b64encode(foto).decode('utf-8')
            else:
                espacio.fotos = foto_original  # Mantén la foto original

            espacio.save()
            return redirect('list')
    else:
        form = EspacioPublicoForm(instance=espacio)

    return render(request, 'edit.html', {'form': form, 'espacio': espacio})


@login_required
def list(request):
    query = request.GET.get('q')
    if query:
        spaces = EspacioPublico.objects.filter(nombre__icontains=query)
    else:
        spaces = EspacioPublico.objects.all()
    # eliminar 'fecha' de la sesion si existe
    if 'fecha' in request.session:
        request.session.pop('fecha')
    return render(request, 'list.html', {'spaces': spaces})


@login_required
@tipo_usuario_requerido('superusuario', 'personal_administrativo')
def create(request):
    estado_choices = EspacioPublico.ESTADO
    if request.method == 'POST':
        form = EspacioPublicoForm(request.POST, request.FILES)
        if form.is_valid():
            espacio = form.save(commit=False)
            if request.FILES.get('fotos'):  # Si se subió una foto
                foto = request.FILES['fotos'].read()
                espacio.fotos = base64.b64encode(foto).decode('utf-8')
            espacio.save()
            return redirect('list')
    else:
        form = EspacioPublicoForm()
    return render(request, 'create.html',
                  {'form': form, 'estado_choices': estado_choices})


@login_required
@tipo_usuario_requerido('superusuario', 'personal_administrativo')
def delete(request, id):
    space = get_object_or_404(EspacioPublico, id=id)
    if request.method == 'POST':
        space.delete()
        return redirect('list')
    return render(request, 'delete.html', {'espacio': space})



@login_required
@tipo_usuario_requerido('superusuario', 'personal_administrativo')
def reservas_fecha(request, id):
    espacio = get_object_or_404(EspacioPublico, id=id)
    fecha_seleccionada = request.GET.get('date') if request.GET.get('date') else request.session.get('fecha')
    if fecha_seleccionada is None:
        fecha_seleccionada = datetime.now().strftime('%Y-%m-%d')
    
    if fecha_seleccionada:
        reservas = Reserva.objects.filter(espacio=espacio, fecha=fecha_seleccionada).order_by('hora_inicio')
    else:
        reservas = Reserva.objects.filter(espacio=espacio).order_by('hora_inicio')
    
    return render(request, 'reservas.html', {
        'espacio': espacio,
        'reservas': reservas,
        'fecha': fecha_seleccionada
    })
