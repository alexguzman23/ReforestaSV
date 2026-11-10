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
]