from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Alumno (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    cI=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    edad=models.PositiveIntegerField()
