"""
URL configuration for ReforestaSV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # <-- Importante para el login

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas de autenticación predeterminadas de Django
    path('accounts/login/', auth_views.LoginView.as_view(template_name='arboles/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # Incluir las rutas de tu aplicación Gestion_Arboles
    path('', include('Gestion_Arboles.urls')),
]