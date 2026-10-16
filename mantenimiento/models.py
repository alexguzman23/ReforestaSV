from django.db import models
from django.conf import settings


class Mantenimiento(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)
    fecha_actividad = models.DateTimeField()
    tipo_actividad = models.CharField(max_length=80)
    comentarios = models.CharField(max_length=255)

    arbol = models.ForeignKey(
        'arbol.Arbol',
        on_delete=models.PROTECT
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    def registrar_mantenimiento(self):
        return f"Mantenimiento: {self.tipo_actividad}"

    def adjuntar_evidencia(self):
        return "Evidencia de mantenimiento"

    @staticmethod
    def consultar_calendario():
        return Mantenimiento.objects.order_by("fecha_actividad")

    def __str__(self):
        return self.tipo_actividad