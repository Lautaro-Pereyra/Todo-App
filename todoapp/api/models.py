from django.db import models

# Create your models here.

class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    realizado = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.nombre