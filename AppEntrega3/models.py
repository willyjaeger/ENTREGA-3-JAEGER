from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    cuit=models.IntegerField()
    direccion=models.CharField(max_length=40)
    def __str__(self):
        return f"{self.nombre} - {self.cuit}"
    

class Provedor(models.Model):
    nombre=models.CharField(max_length=40)
    cuit=models.IntegerField()
    direccion=models.CharField(max_length=40) 
    def __str__(self):
        return f"{self.nombre} - {self.cuit}"   

class Articulo(models.Model):
    descripcion =models.CharField(max_length=50)
    marca =models.CharField(max_length=40)    
    def __str__(self):
        return f"{self.descripcion} - {self.marca}"
class Compras(models.Model):
    fecha=models.DateField()
    nfactura=models.CharField(max_length=15)
    provedor=models.CharField(max_length=40)
    importe=models.DecimalField(max_digits=20, decimal_places=2)         
    def __str__(self):
        return f"{self.fecha} -{self.provedor} - {self.nfactura} - {self.importe}"