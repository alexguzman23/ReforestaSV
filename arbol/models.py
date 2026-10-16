from django.db import models


class Arbol(models.Model):
    codigo_unico = models.CharField(max_length=80, unique=True)
    fecha_plantacion = models.DateField()
    estado_salud = models.CharField(max_length=50)

    campana = models.ForeignKey(
        'CampanaReforestacion.CampanaReforestacion',
        on_delete=models.PROTECT
    )

    especie = models.ForeignKey(
        'especie.Especie',
        on_delete=models.PROTECT
    )

    ubicacion = models.ForeignKey(
        'ubicacion.Ubicacion',
        on_delete=models.PROTECT
    )

    responsable = models.ForeignKey(
        'responsable.Responsable',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def registrar_arbol(self):
        return f"Árbol: {self.codigo_unico}"

    def actualizar_estado(self, nuevo_estado):
        estados = ["Activo/Sano", "Dañado", "Perdido/Seco"]

        if nuevo_estado not in estados:
            raise ValueError("Estado no válido")

        self.estado_salud = nuevo_estado

    @staticmethod
    def filtrar_inventario():
        return Arbol.objects.all()

    def __str__(self):
        return self.codigo_unico