# trabajadores/models.py

from django.db import models

class Cargo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cargo'

class Trabajador(models.Model):
    rut = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rut} - {self.nombre}"

    class Meta:
        db_table = 'trabajador'

class Documento(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='documentos/')
    fecha_emision = models.DateField()
    fecha_termino = models.DateField()

    def __str__(self):
        return f"{self.archivo} ({self.fecha_emision} - {self.fecha_termino})"

    class Meta:
        db_table = 'documento'
