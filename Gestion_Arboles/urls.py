from django.urls import path
from . import views

urlpatterns = [
    path('', views.arbol_list, name='arbol_list'),
    path('nuevo/', views.arbol_create, name='arbol_create'),
    path('editar/<int:pk>/', views.arbol_update, name='arbol_update'),
    path('eliminar/<int:pk>/', views.arbol_delete, name='arbol_delete'),
]