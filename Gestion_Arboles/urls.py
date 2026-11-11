
from django.urls import path
from . import views

urlpatterns = [
    # Menú principal
    path('', views.inicio, name='inicio'),

    # Rutas de Árboles
    path('inventario/', views.arbol_list, name='arbol_list'),
    path('nuevo/', views.arbol_create, name='arbol_create'),
    path('editar/<int:pk>/', views.arbol_update, name='arbol_update'),
    path('eliminar/<int:pk>/', views.arbol_delete, name='arbol_delete'),

    # Rutas de Especies Nativas
    path('especies/', views.especie_list, name='especie_list'),
    path('especies/nueva/', views.especie_create, name='especie_create'),
    path('especies/editar/<int:pk>/', views.especie_update, name='especie_update'),
    path('especies/eliminar/<int:pk>/', views.especie_delete, name='especie_delete'),

    # Rutas de Ubicaciones
    path('ubicaciones/', views.ubicacion_list, name='ubicacion_list'),
    path('ubicaciones/nueva/', views.ubicacion_create, name='ubicacion_create'),
    path('ubicaciones/editar/<int:pk>/', views.ubicacion_update, name='ubicacion_update'),
    path('ubicaciones/eliminar/<int:pk>/', views.ubicacion_delete, name='ubicacion_delete'),

    # Rutas de Mantenimiento
    path('mantenimiento/', views.mantenimiento_list, name='mantenimiento_list'),
    path('mantenimiento/nuevo/', views.mantenimiento_create, name='mantenimiento_create'),
    path('mantenimiento/editar/<int:pk>/', views.mantenimiento_update, name='mantenimiento_update'),
    path('mantenimiento/eliminar/<int:pk>/', views.mantenimiento_delete, name='mantenimiento_delete'),

    # Rutas de Responsables
    path('responsables/', views.responsable_list, name='responsable_list'),
    path('responsables/nuevo/', views.responsable_create, name='responsable_create'),
    path('responsables/editar/<int:pk>/', views.responsable_update, name='responsable_update'),
    path('responsables/eliminar/<int:pk>/', views.responsable_delete, name='responsable_delete'),
]
