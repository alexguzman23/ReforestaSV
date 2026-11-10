from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Arbol, Especie, Ubicacion
from .forms import ArbolForm, EspecieForm, UbicacionForm
from django.db.models.deletion import ProtectedError


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
# CRUD UBICACIONES
# ==========================================

# 1. CONSULTAR UBICACIONES
def ubicacion_list(request):
    ubicaciones = Ubicacion.objects.all()

    return render(request, 'ubicaciones/ubicacion_list.html', {
        'ubicaciones': ubicaciones
    })

# 2. REGISTRAR UBICACIÓN
def ubicacion_create(request):
    if request.method == 'POST':
        form = UbicacionForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Ubicación registrada exitosamente.'
            )
            return redirect('ubicacion_list')
    else:
        form = UbicacionForm()

    return render(request, 'ubicaciones/ubicacion_form.html', {
        'form': form,
        'titulo': 'Registrar Ubicación'
    })

# 3. MODIFICAR UBICACIÓN
def ubicacion_update(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)

    if request.method == 'POST':
        form = UbicacionForm(request.POST, instance=ubicacion)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Ubicación actualizada correctamente.'
            )
            return redirect('ubicacion_list')
    else:
        form = UbicacionForm(instance=ubicacion)

    return render(request, 'ubicaciones/ubicacion_form.html', {
        'form': form,
        'titulo': 'Modificar Ubicación'
    })

# 4. ELIMINAR UBICACIÓN
def ubicacion_delete(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)

    if request.method == 'POST':
        try:
            ubicacion.delete()
            messages.success(
                request,
                'Ubicación eliminada correctamente.'
            )
        except ProtectedError:
            messages.error(
                request,
                'No se puede eliminar esta ubicación porque tiene árboles asociados.'
            )

        return redirect('ubicacion_list')

    return render(
        request,
        'ubicaciones/ubicacion_confirm_delete.html',
        {'ubicacion': ubicacion}
    )

# ==========================================
# VISTA INICIO
# ==========================================
@login_required(login_url='/accounts/login/')
def inicio(request):
    return render(request, 'arboles/inicio.html')

