from django.db import models
from trabajadores.models import Trabajador, Documento

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=200)
    nombre_faena = models.CharField(max_length=200)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    documentos = models.ManyToManyField(Documento)

    def __str__(self):
        return self.nombre_proyecto
