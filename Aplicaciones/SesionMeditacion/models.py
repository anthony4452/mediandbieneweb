from django.db import models
from django.conf import settings
from Aplicaciones.Proposito.models import Proposito

class SesionMeditacion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    proposito = models.ForeignKey(Proposito, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    duracion_minutos = models.IntegerField()
    calificacion = models.IntegerField()

    def __str__(self):
        return f"{self.usuario.username} - {self.fecha} ({self.calificacion}/10)"
