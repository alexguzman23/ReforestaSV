
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.db.models.deletion import ProtectedError

from .models import CampanaReforestacion
from .forms import CampanaReforestacionForm


def inicio(request):
    return HttpResponse("Bienvenidos a ReforestaSV")


# 1. CONSULTAR CAMPAÑAS
def campana_list(request):
    campanas = CampanaReforestacion.objects.all()
    return render(request, 'campanas/campana_list.html', {'campanas': campanas})


# 2. REGISTRAR CAMPAÑA
def campana_create(request):
    form = CampanaReforestacionForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Campaña registrada correctamente.')
        return redirect('campana_list')

    return render(request, 'campanas/campana_form.html', {
        'form': form,
        'titulo': 'Nueva Campaña'
    })


# 3. ACTUALIZAR CAMPAÑA
def campana_update(request, pk):
    campana = get_object_or_404(CampanaReforestacion, pk=pk)
    form = CampanaReforestacionForm(request.POST or None, instance=campana)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Campaña actualizada correctamente.')
        return redirect('campana_list')

    return render(request, 'campanas/campana_form.html', {
        'form': form,
        'titulo': 'Editar Campaña'
    })


# 4. ELIMINAR CAMPAÑA
def campana_delete(request, pk):
    campana = get_object_or_404(CampanaReforestacion, pk=pk)

    if request.method == 'POST':
        try:
            campana.delete()
            messages.success(request, 'Campaña eliminada correctamente.')

        except ProtectedError:
            messages.error(
                request,
                'No se puede eliminar esta campaña porque tiene árboles registrados.'
            )

        return redirect('campana_list')

    return render(request, 'campanas/campana_confirm_delete.html', {
        'campana': campana
    })
