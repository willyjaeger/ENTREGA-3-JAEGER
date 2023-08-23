from django.contrib import admin
from.models import Articulo, Cliente , Provedor, Compras

# Register your models here.
admin.site.register(Articulo)
admin.site.register(Provedor)
admin.site.register(Cliente)
admin.site.register(Compras)