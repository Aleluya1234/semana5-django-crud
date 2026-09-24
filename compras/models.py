from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    cantidad = models.PositiveIntegerField(default=1)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.cantidad})"
