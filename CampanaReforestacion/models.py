from django.db import models

# Create your models here.
class CampanaReforestacion(models.Model):
     id_campana = models.AutoField(primary_key=True)
     nombre = models.CharField(max_length=120)
     fecha_inicio = models.DateField()
     institucion_beneficiaria = models.CharField(max_length=150)
     cantidad_proyectada = models.IntegerField()

def registrar_campana(self):
        return f"Campaña {self.nombre} registrada"

def modificar_campana(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        return self.nombre

def consultar_progreso(self):
        return self.arboles.count()

def __str__(self):
        return self.nombre
     