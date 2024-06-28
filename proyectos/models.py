# proyectos/models.py

'''from django.db import models
from trabajadores.models import Trabajador

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=100)
    nombre_faena = models.CharField(max_length=100)
    trabajadores = models.ManyToManyField(Trabajador, through='AsignacionProyecto')

    def __str__(self):
        return self.nombre_proyecto

    class Meta:
        db_table = 'proyecto'

class ProyectoTrabajadores(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.proyecto.nombre_proyecto} - {self.trabajador.nombre}"


class AsignacionProyecto(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    class Meta:
        db_table = 'asignacion_proyecto'
'''

from django.db import models
from trabajadores.models import Trabajador

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=100)
    nombre_faena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_proyecto
    
    class Meta:
        db_table = 'proyecto'

class ProyectoTrabajadores(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.proyecto} - {self.trabajador}"

    class Meta:
        db_table = 'proyecto_trabajadores'