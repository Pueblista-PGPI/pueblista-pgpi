from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .decorators import tipo_usuario_requerido
from .models import EspacioPublico
from .forms import EspacioPublicoForm


@login_required
@tipo_usuario_requerido('superusuario', 'personal_administrativo')
def edit(request, id):
    espacio = get_object_or_404(EspacioPublico, id=id)
    if request.method == 'POST':
        # Lógica para manejar la edición del espacio
        # Por ejemplo, actualizar los campos del espacio
        espacio.nombre = request.POST.get('nombre')
        espacio.horario = request.POST.get('horario')
        espacio.descripcion = request.POST.get('descripcion')
        espacio.telefono = request.POST.get('telefono')
        espacio.estado = request.POST.get('estado')
        if 'fotos' in request.FILES:
            espacio.fotos = request.FILES['fotos']
        espacio.save()
        return redirect('list')
    return render(request, 'edit.html', {'espacio': espacio})


@login_required
def list(request):
    spaces = EspacioPublico.objects.all()
    return render(request, 'list.html', {'spaces': spaces})


@login_required
@tipo_usuario_requerido('superusuario', 'personal_administrativo')
def create(request):
    estado_choices = EspacioPublico.ESTADO
    if request.method == 'POST':
        form = EspacioPublicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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
