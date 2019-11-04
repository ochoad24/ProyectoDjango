from django.db import models
from django.utils import timezone
# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=200)
    created_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=200)
    precio_compra=models.FloatField()
    precio_venta=models.FloatField()
    existencia=models.IntegerField()
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    created_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    telefono=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    direccion=models.CharField(max_length=200)
    created_date=models.DateTimeField(default=timezone.now)

class Encabezado(models.Model):
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    total=models.FloatField()
    created_date=models.DateTimeField(default=timezone.now)
    estado=models.BooleanField()

class Detalle(models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    encabezado=models.ForeignKey(Encabezado,on_delete=models.CASCADE)
    subtotal=models.FloatField()
    cantidad=models.IntegerField()
    precio_venta=models.FloatField()
    