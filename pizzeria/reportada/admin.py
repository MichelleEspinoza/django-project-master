from django.contrib import admin
from .models import *
# Register your models here.

# @admin.register(SignUpUsersForm)
# class AdminRegistro(admin.ModelAdmin):
# 	list_display=[
# 		'first_name',
# 		'last_name',
# 		'email',
# 	]

# @admin.register(Registro)
# class AdminRegistro(admin.ModelAdmin):
# 	list_display=[
# 	    "first_name",
# 		"last_name",
# 		"email",
# 		"username",
# 		"password1",
# 		"password2",
# 	]

@admin.register(Usuarios)
class AdminUsuarios(admin.ModelAdmin):
	list_display=[
 		'user',
		'middle_name',
		'fecha_nacimiento',
	]

@admin.register(Direcciones)
class AdminDirecciones(admin.ModelAdmin):
	list_display=[
 		'usuario',
	    'nombre_calle',
	    'tipo_calle',
	    'num_casa',
	    'colonia',
	    'codigo_postal',
	    'ciudad',
	]

@admin.register(Empleados)
class AdminEmpleados(admin.ModelAdmin):
	list_display=[
 		'usuario',
	    'curp',
	    'rfc',
	    'nss',
	    'sexo',
	]

@admin.register(Clientes)
class AdminClientes(admin.ModelAdmin):
	list_display=[
	    'usuario',
	    'pago_por_defecto',
	    'paypal',
	]

@admin.register(Cards)
class AdminCards(admin.ModelAdmin):
	list_display=[
	    'cliente',
		'numero',
		'ccv',
	]

@admin.register(Productos)
class AdminProductos(admin.ModelAdmin):
	list_display=[
	    'descripcion',
	    'precio',
	    'size',
	]

@admin.register(Ventas)
class AdminVentas(admin.ModelAdmin):
	list_display=[
	    'cliente',
	    
	    'estatus',
	    'fecha',
	    'impuesto',
	    'subtotal',
	]

@admin.register(VentasDetalle)
class AdminVentasDetalle(admin.ModelAdmin):
	list_display=[
	    'venta',
	    'producto',
	    'cantidad',
	]