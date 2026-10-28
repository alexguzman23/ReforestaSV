from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Arbol
from .forms import ArbolForm

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