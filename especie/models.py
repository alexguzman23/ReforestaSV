from django.db import models


class Especie(models.Model):
    id_especie = models.AutoField(primary_key=True)
    nombre_comun = models.CharField(max_length=100)
    nombre_cientifico = models.CharField(max_length=150)
    requerimientos_riego = models.CharField(max_length=255)

    def registrar_especie(self):
        return f"Especie: {self.nombre_comun}"

    def consultar_ficha(self):
        return f"{self.nombre_comun} - {self.nombre_cientifico}"

    def __str__(self):
        return self.nombre_comun