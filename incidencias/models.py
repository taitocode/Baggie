from django.db import models

from productos.models import Producto
from empaques.models import Empaque
from usuarios.models import Usuario

# Create your models here.


class Incidencia(models.Model):
    Fecha = models.DateTimeField(auto_now_add=True)
    Descripcion = models.CharField(max_length=25)
    Empaque = models.ForeignKey(Empaque, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
