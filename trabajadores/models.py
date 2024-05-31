from django.db import models

class Cargo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=20)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Documento(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='documentos/')
    fecha_emision = models.DateField()
    fecha_termino = models.DateField()

    def __str__(self):
        return self.archivo.name
