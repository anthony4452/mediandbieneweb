from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuarios(AbstractUser):
    ROLES = (
        ('ADMINISTRADOR', 'Administrador'),
        ('USUARIO', 'Usuario'),
    )
    rol = models.CharField(max_length=20, choices=ROLES, default='USUARIO')
