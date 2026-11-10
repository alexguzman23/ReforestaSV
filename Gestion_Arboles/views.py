from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Arbol, Especie
from .forms import ArbolForm, EspecieForm

# ==========================================
# CRUD ÁRBOLES
# ==========================================

# 1. CONSULTAR (Listar)
def arbol_list(request):
    arboles = Arbol.objects.select_related('campana', 'especie', 'ubicacion', 'responsable').all()
    return render(request, 'arboles/arbol_list.html', {'arboles': arboles})

# 2. REGISTRAR (Crear)
def arbol_create(request):
    if request.method == 'POST':
        form = ArbolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Árbol registrado exitosamente.')
            return redirect('arbol_list')
    else:
        form = ArbolForm()
    return render(request, 'arboles/arbol_form.html', {'form': form, 'titulo': 'Registrar Árbol'})

# 3. MODIFICAR (Editar)
def arbol_update(request, pk):
    arbol = get_object_or_404(Arbol, pk=pk)
    if request.method == 'POST':
        form = ArbolForm(request.POST, instance=arbol)
        if form.is_valid():
            form.save()
            messages.success(request, 'Árbol actualizado correctamente.')
            return redirect('arbol_list')
    else:
        form = ArbolForm(instance=arbol)
    return render(request, 'arboles/arbol_form.html', {'form': form, 'titulo': 'Modificar Árbol'})

# 4. ELIMINAR
def arbol_delete(request, pk):
    arbol = get_object_or_404(Arbol, pk=pk)
    if request.method == 'POST':
        arbol.delete()
        messages.success(request, 'Árbol eliminado correctamente.')
        return redirect('arbol_list')
    return render(request, 'arboles/arbol_confirm_delete.html', {'arbol': arbol})


# ==========================================
# CRUD ESPECIES
# ==========================================

# 1. CONSULTAR ESPECIES
def especie_list(request):
    especies = Especie.objects.all()
    return render(request, 'arboles/especie_list.html', {'especies': especies})

# 2. REGISTRAR ESPECIE
def especie_create(request):
    if request.method == 'POST':
        form = EspecieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Especie registrada exitosamente.')
            return redirect('especie_list')
    else:
        form = EspecieForm()
    return render(request, 'arboles/especie_form.html', {'form': form, 'titulo': 'Registrar Especie'})

# 3. MODIFICAR ESPECIE
def especie_update(request, pk):
    especie = get_object_or_404(Especie, pk=pk)
    if request.method == 'POST':
        form = EspecieForm(request.POST, instance=especie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Especie actualizada correctamente.')
            return redirect('especie_list')
    else:
        form = EspecieForm(instance=especie)
    return render(request, 'arboles/especie_form.html', {'form': form, 'titulo': 'Modificar Especie'})

# 4. ELIMINAR ESPECIE
def especie_delete(request, pk):
    especie = get_object_or_404(Especie, pk=pk)
    if request.method == 'POST':
        especie.delete()
        messages.success(request, 'Especie eliminada correctamente.')
        return redirect('especie_list')
    return render(request, 'arboles/especie_confirm_delete.html', {'especie': especie})


# ==========================================
# VISTA INICIO
# ==========================================
@login_required(login_url='/accounts/login/')
def inicio(request):
    return render(request, 'arboles/inicio.html')