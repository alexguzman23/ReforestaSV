from django.db import models
from django.conf import settings

#Clase Arbol
class Arbol(models.Model):
    codigo_unico = models.CharField(max_length=80, unique=True)
    fecha_plantacion = models.DateField()
    estado_salud = models.CharField(max_length=50)

    campana = models.ForeignKey(
        'CampanaReforestacion.CampanaReforestacion',
        on_delete=models.PROTECT
    )

    especie = models.ForeignKey(
        'Gestion_Arboles.Especie',
        on_delete=models.PROTECT
    )

    ubicacion = models.ForeignKey(
        'Gestion_Arboles.Ubicacion',
        on_delete=models.PROTECT
    )

    responsable = models.ForeignKey(
        'Gestion_Arboles.Responsable',
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

    #Clase especie
    
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

#Clase Ubicacion
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

#Clase Responsable
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
#Clase Mantenimiento
class Mantenimiento(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)
    fecha_actividad = models.DateTimeField()
    tipo_actividad = models.CharField(max_length=80)
    comentarios = models.CharField(max_length=255)

    arbol = models.ForeignKey(
        'Gestion_Arboles.Arbol',
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



