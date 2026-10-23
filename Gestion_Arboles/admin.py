from django.contrib import admin

# Register your models here.

from .models import (
    Arbol,
    Especie,
    Ubicacion,
    Responsable,
    Mantenimiento
)

admin.site.register(Arbol)
admin.site.register(Especie)
admin.site.register(Ubicacion)
admin.site.register(Responsable)
admin.site.register(Mantenimiento)