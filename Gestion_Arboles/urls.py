from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'), # El menú principal de la app
    path('inventario/', views.arbol_list, name='arbol_list'), # La tabla de árboles ahora estará aquí
    path('nuevo/', views.arbol_create, name='arbol_create'),
    path('editar/<int:pk>/', views.arbol_update, name='arbol_update'),
    path('eliminar/<int:pk>/', views.arbol_delete, name='arbol_delete'),
    path('registro/', views.register, name='register'),
]