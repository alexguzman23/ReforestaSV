from django.db import models


class Responsable(models.Model):
    id_responsable = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    rol_asignado = models.CharField(max_length=80)
    contacto = models.CharField(max_length=120)

    def asignar_zona(self):
        return f"Responsable: {self.nombre}"

    def verificar_supervision(self):
        return f"Supervisión de: {self.nombre}"

    def __str__(self):
        return self.nombre