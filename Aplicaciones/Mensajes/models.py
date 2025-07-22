from django.db import models
from Aplicaciones.Usuarios.models import Usuarios
from Aplicaciones.Proposito.models import Proposito
from Aplicaciones.SesionMeditacion.models import SesionMeditacion

# Create your models here.
class Mensaje(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    destinatario = models.EmailField()
    asunto = models.TextField(max_length=100)
    mensaje = models.TextField(max_length=1000)
    archivo = models.FileField(upload_to='archivos/', blank=True)
    factura = models.FileField(upload_to='facturas/', blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"(self.titulo)"
