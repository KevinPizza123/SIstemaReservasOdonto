from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    recordatorio_enviado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.paciente.nombre} - {self.fecha} a las {self.hora}"
