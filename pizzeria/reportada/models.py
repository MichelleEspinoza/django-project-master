from django.db import models
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class Registro(models.Model):
	first_name=models.CharField(settings.AUTH_USER_MODEL,max_length=150)
	last_name=models.CharField(max_length=150)
	email= models.EmailField(max_length=150, blank=True)
	username= models.CharField(max_length=150)
	password1=models.CharField(max_length=150)
	password2=models.CharField(max_length=150)

	

class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username
    # first_name
    middle_name = models.CharField(max_length=150, blank=True)
    # last_name
    # email
    # password
    fecha_nacimiento = models.DateField(blank=True)
    # is_staff
    # is_active

class Direcciones(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    nombre_calle = models.CharField(max_length=40)
    tipo_calle = models.CharField(max_length=20)
    num_casa = models.CharField(max_length=6, blank=True)
    colonia = models.CharField(max_length=40)
    codigo_postal = models.CharField(max_length=6)
    ciudad = models.CharField(max_length=20)

class Empleados(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    curp = models.CharField(max_length=18)
    rfc = models.CharField(max_length=13)
    nss = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1)

class Clientes(models.Model):
    METODOS_PAGO = [
        ('Efectivo', 'Efectivo'),
        ('Paypal', 'Paypal'),
        ('Tarjeta de Credito/Debito', 'Tarjeta de Credito/Debito'),
    ]
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    pago_por_defecto = models.CharField(max_length=25, choices=METODOS_PAGO)
    paypal = models.EmailField(max_length=64, blank=True)

class Cards(models.Model):
	cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
	numero = models.CharField(max_length=16)
	ccv = models.CharField(max_length=4)

class Productos(models.Model):
    SIZE_PIZZA = [
        ('Individual', 'Individual'),
        ('Mediana', 'Mediana'),
        ('Grande', 'Grande'),
        ('Familiar', 'Familiar'),
    ]
    descripcion = models.CharField(max_length=128)
    precio = models.FloatField()
    size = models.CharField(max_length=10, choices=SIZE_PIZZA, blank=True)
    
class Ventas(models.Model):
    ESTATUS_VENTA = [
        ('Pendiente', 'Pendiente'),
        ('Cancelada', 'Cancelada'),
        ('Finalizada', 'Finalizada'),
    ]
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Productos, through='VentasDetalle')
    estatus = models.CharField(max_length=10, choices=ESTATUS_VENTA)
    fecha = models.DateTimeField(auto_now_add=True)
    impuesto = models.FloatField()  # IVA en dinero    16%
    subtotal = models.FloatField()

class VentasDetalle(models.Model):
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

