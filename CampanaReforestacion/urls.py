from django.urls import path
from . import views

urlpatterns = [
    path('', views.campana_list, name='campana_list'),
    path('crear/', views.campana_create, name='campana_create'),
    path('editar/<int:pk>/', views.campana_update, name='campana_update'),
    path('eliminar/<int:pk>/', views.campana_delete, name='campana_delete'),
]