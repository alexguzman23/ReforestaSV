from django.db import models


class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=7)
    longitud = models.DecimalField(max_digits=10, decimal_places=7)
    zona_referencia = models.CharField(max_length=150)

    def registrar_ubicacion(self):
        return f"Ubicación: {self.zona_referencia}"

    def obtener_coordenadas(self):
        return self.latitud, self.longitud

    def __str__(self):
        return self.zona_referencia
