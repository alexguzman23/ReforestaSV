
from django.db import models
from django.conf import settings


class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    def cantidad_usuarios(self):
        return self.perfiles.count()


class Permiso(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="perfil"
    )
    rol = models.ForeignKey(
        Rol,
        on_delete=models.PROTECT,
        related_name="perfiles"
    )
    permisos = models.ManyToManyField(
        Permiso,
        blank=True,
        related_name="perfiles"
    )
    telefono = models.CharField(max_length=20, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.rol.nombre}"

    def tiene_permiso(self, nombre_permiso):
        return self.permisos.filter(
            nombre=nombre_permiso
        ).exists()

    def desactivar(self):
        self.activo = False
        self.save()


