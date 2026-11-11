from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Bienvenidos a ReforestaSV")

from django.shortcuts import render, redirect, get_object_or_404
from .models import CampanaReforestacion
from .forms import CampanaReforestacionForm

def campana_list(request):
    campanas = CampanaReforestacion.objects.all()
    return render(request, 'campanas/campana_list.html', {'campanas': campanas})

def campana_create(request):
    form = CampanaReforestacionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('campana_list')
    return render(request, 'campanas/campana_form.html', {'form': form, 'titulo': 'Nueva Campaña'})

def campana_update(request, pk):
    campana = get_object_or_404(CampanaReforestacion, pk=pk)
    form = CampanaReforestacionForm(request.POST or None, instance=campana)
    if form.is_valid():
        form.save()
        return redirect('campana_list')
    return render(request, 'campanas/campana_form.html', {'form': form, 'titulo': 'Editar Campaña'})

def campana_delete(request, pk):
    campana = get_object_or_404(CampanaReforestacion, pk=pk)
    if request.method == 'POST':
        campana.delete()
        return redirect('campana_list')
    return render(request, 'campanas/campana_confirm_delete.html', {'campana': campana})