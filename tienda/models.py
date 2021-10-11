from django.db import models
from productos.models import Producto

# Create your models here.

class TituloPag(models.Model):
    titulo =  models.CharField(max_length=200,verbose_name='Titulo de Pag')

    def __str__(self):
        return self.titulo


class CheckoutClientes(models.Model):
    nombre = models.CharField(max_length=300,verbose_name='Nombre')
    apellido = models.CharField(max_length=300,verbose_name='Apellido')
    dni = models.IntegerField(verbose_name='DNI')
    direc = models.CharField(max_length=300,verbose_name='Direccion')
    loc = models.CharField(max_length=300,verbose_name='Localidad')
    provincias= (
        ('C.A.B.A.','C.A.B.A.'),
        ('Buenos Aires','Buenos Aires',),
        ('Catamarca','Catamarca'),
        ('Chaco','Chaco'),
        ('Chubut','Chubut'),
        ('Córdoba','Córdoba'),
        ('Corrientes','Corrientes'),
        ('Entre Ríos','Entre Ríos'),
        ('Formosa','Formosa'),
        ('Jujuy','Jujuy'),
        ('La Pampa','La Pampa'),
        ('La Rioja','La Rioja'),
        ('Mendoza','Mendoza'),
        ('Misiones','Misiones'),
        ('Neuquén','Neuquén'),
        ('Río Negro','Río Negro'),
        ('Salta','Salta'),
        ('San Juan','San Juan'),
        ('Santa Cruz','Santa Cruz'),
        ('Santa Fe','Santa Fe'),
        ('Santiago del Estero','Santiago del Estero'),
        ('Tierra del Fuego','Tierra del Fuego'),
        ('Tucumán','Tucumán'),
    )
    pcia = models.CharField(max_length=300,choices=provincias, verbose_name='Provincia')
    tlf = models.IntegerField(verbose_name='Telefono')
    transp = models.CharField(max_length=300,verbose_name='Trasporte',default='N/A')

    def __str__(self):
        return self.nombre



    
