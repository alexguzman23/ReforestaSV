from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Arbol, Especie, Ubicacion, Responsable
from .forms import ArbolForm, EspecieForm, UbicacionForm, ResponsableForm
from django.db.models.deletion import ProtectedError
from django.db.models import Q
from django.utils import timezone

from .models import Mantenimiento
from .forms import MantenimientoForm


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
# CRUD DE MANTENIMIENTO
# ==========================================


# 1. CONSULTAR MANTENIMIENTOS
@login_required
def mantenimiento_list(request):

    mantenimientos = Mantenimiento.objects.select_related(
        "arbol",
        "arbol__especie",
        "usuario"
    ).order_by("-fecha_actividad")

    # Parámetros de búsqueda
    busqueda = request.GET.get("buscar", "").strip()
    tipo_seleccionado = request.GET.get("tipo", "").strip()

    # Buscar por código o especie
    if busqueda:
        mantenimientos = mantenimientos.filter(
            Q(arbol__codigo_unico__icontains=busqueda) |
            Q(arbol__especie__nombre_comun__icontains=busqueda)
        )

    # Filtrar por tipo de actividad
    if tipo_seleccionado:
        mantenimientos = mantenimientos.filter(
            tipo_actividad=tipo_seleccionado
        )

    # Tipos disponibles para el filtro
    tipos = (
        Mantenimiento.objects
        .order_by("tipo_actividad")
        .values_list("tipo_actividad", flat=True)
        .distinct()
    )

    # Estadísticas generales
    total_mantenimientos = Mantenimiento.objects.count()

    realizados_hoy = Mantenimiento.objects.filter(
        fecha_actividad__date=timezone.localdate()
    ).count()

    arboles_atendidos = (
        Mantenimiento.objects
        .values("arbol_id")
        .distinct()
        .count()
    )

    contexto = {
        "mantenimientos": mantenimientos,
        "busqueda": busqueda,
        "tipo_seleccionado": tipo_seleccionado,
        "tipos": tipos,
        "total_mantenimientos": total_mantenimientos,
        "realizados_hoy": realizados_hoy,
        "arboles_atendidos": arboles_atendidos,
    }

    return render(
        request,
        "arboles/mantenimiento_list.html",
        contexto
    )


# 2. REGISTRAR MANTENIMIENTO
@login_required
def mantenimiento_create(request):

    if request.method == "POST":
        form = MantenimientoForm(request.POST)

        if form.is_valid():
            mantenimiento = form.save(commit=False)

            # Usuario que inició sesión
            mantenimiento.usuario = request.user

            mantenimiento.save()

            messages.success(
                request,
                "Mantenimiento registrado correctamente."
            )

            return redirect("mantenimiento_list")

    else:
        form = MantenimientoForm()

    return render(
        request,
        "arboles/mantenimiento_form.html",
        {
            "form": form,
            "titulo": "Registrar mantenimiento"
        }
    )


# 3. MODIFICAR MANTENIMIENTO
@login_required
def mantenimiento_update(request, pk):

    mantenimiento = get_object_or_404(
        Mantenimiento,
        pk=pk
    )

    if request.method == "POST":
        form = MantenimientoForm(
            request.POST,
            instance=mantenimiento
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Mantenimiento actualizado correctamente."
            )

            return redirect("mantenimiento_list")

    else:
        form = MantenimientoForm(
            instance=mantenimiento
        )

    return render(
        request,
        "arboles/mantenimiento_form.html",
        {
            "form": form,
            "titulo": "Modificar mantenimiento",
            "mantenimiento": mantenimiento
        }
    )


# 4. ELIMINAR MANTENIMIENTO
@login_required
def mantenimiento_delete(request, pk):

    mantenimiento = get_object_or_404(
        Mantenimiento,
        pk=pk
    )

    if request.method == "POST":

        mantenimiento.delete()

        messages.success(
            request,
            "Mantenimiento eliminado correctamente."
        )

        return redirect("mantenimiento_list")

    return render(
        request,
        "arboles/mantenimiento_confirm_delete.html",
        {
            "mantenimiento": mantenimiento
        }
    )

# ==========================================
# CRUD DE RESPONSABLES
# ==========================================

# 1. CONSULTAR RESPONSABLES
def responsable_list(request):
    responsables = Responsable.objects.all()

    return render(
        request,
        'responsables/responsable_list.html',
        {'responsables': responsables}
    )


# 2. REGISTRAR RESPONSABLE
def responsable_create(request):
    if request.method == 'POST':
        form = ResponsableForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Responsable registrado exitosamente.'
            )

            return redirect('responsable_list')

    else:
        form = ResponsableForm()

    return render(
        request,
        'responsables/responsable_form.html',
        {
            'form': form,
            'titulo': 'Registrar Responsable'
        }
    )


# 3. MODIFICAR RESPONSABLE
def responsable_update(request, pk):
    responsable = get_object_or_404(Responsable, pk=pk)

    if request.method == 'POST':
        form = ResponsableForm(
            request.POST,
            instance=responsable
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Responsable actualizado correctamente.'
            )

            return redirect('responsable_list')

    else:
        form = ResponsableForm(instance=responsable)

    return render(
        request,
        'responsables/responsable_form.html',
        {
            'form': form,
            'titulo': 'Modificar Responsable'
        }
    )


# 4. ELIMINAR RESPONSABLE
def responsable_delete(request, pk):
    responsable = get_object_or_404(Responsable, pk=pk)

    if request.method == 'POST':
        responsable.delete()

        messages.success(
            request,
            'Responsable eliminado correctamente.'
        )

        return redirect('responsable_list')

    return render(
        request,
        'responsables/responsable_confirm_delete.html',
        {'responsable': responsable}
    )



# ==========================================
# VISTA INICIO
# ==========================================
@login_required(login_url='/accounts/login/')
def inicio(request):
    return render(request, 'arboles/inicio.html')


