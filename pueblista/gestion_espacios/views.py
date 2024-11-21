import os
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from gestion_usuarios.decorators import tipo_usuario_requerido
from pueblista import settings
from .models import EspacioPublico
from .forms import EspacioPublicoForm
from gestion_reservas.models import Reserva


@login_required
@tipo_usuario_requerido('superusuario', 'personal_administrativo')
def edit(request, id):
    espacio = get_object_or_404(EspacioPublico, id=id)
    if request.method == 'POST':
        form = EspacioPublicoForm(request.POST, request.FILES, instance=espacio)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EspacioPublicoForm(instance=espacio)
    return render(request, 'edit.html', {'form': form, 'espacio': espacio})


@login_required
def list(request):
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
        foto_path = os.path.join(settings.MEDIA_ROOT, "spaces/"+str(space.fotos))
        if os.path.isfile(foto_path):
            os.remove(foto_path)
        return redirect('list')
    return render(request, 'delete.html', {'espacio': space})


@login_required
@tipo_usuario_requerido('superusuario', 'personal_administrativo')
def reservas(request, id):
    espacio = get_object_or_404(EspacioPublico, pk=id)
    reservas = Reserva.objects.filter(espacio=espacio)
    return render(request, 'reservas.html', {'reservas': reservas, 'espacio': espacio})


@login_required
@tipo_usuario_requerido('superusuario', 'personal_administrativo')
def reservas_fecha(request, espacio_id):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    reservas = Reserva.objects.filter(espacio_id=espacio_id)
    if start_date and end_date:
        reservas = reservas.filter(
            fecha__range=[start_date, end_date]
        )
    elif start_date:
        reservas = reservas.filter(fecha__gte=start_date)
    elif end_date:
        reservas = reservas.filter(fecha__lte=end_date)

    return render(request, 'reservas.html', {
        'reservas': reservas,
        'espacio': EspacioPublico.objects.get(id=espacio_id),
    })
