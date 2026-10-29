from django.db import models

class Cita(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.TimeField()
    codigo = models.CharField(max_length=4, unique=True)
    activa = models.BooleanField(default=True)
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cita {self.codigo} - {self.nombre} ({self.fecha} {self.hora})"
