from django.urls import path
from .views import *

urlpatterns = [ 
path('inicio/', inicio,name="inicio"),
path('crear_provedor/', crear_provedor),
path('provedores/', provedores, name="provedores"),
path('clientes/', clientes,name="clientes"),
path('articulos/', articulos, name="articulos"),
path('compras/', compras,name="compras"),
path('busquedacliente/', busquedacliente, name="busquedacliente"),
path('buscar/', buscar, name="buscar"),
path('listarclientes/', listarclientes, name="listarclientes"),

]