from django.shortcuts import render
from .models import Cliente, Provedor,Articulo,Compras 
from django.http import HttpResponse
from .forms import ComprasForm, ProvedorForm, ArticuloForm, ClienteForm
from django.template import loader


# Create your views here.
def crear_provedor(self):
    provedor = Provedor(nombre="Quilmes",cuit=30456780983,direccion="America 2308")
    provedor.save()
    documentodetexto = ( "----> Provedor {provedor.nombre} Direccion {provedor.direccion}")

    return HttpResponse(documentodetexto)

def inicio(request):
    return render(request,"inicio.html")

def clientes(request):
    if request.method == "POST":
        form=ClienteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            cuit=info["cuit"]
            direccion=info["direccion"]
            cliente=Cliente(nombre=nombre,cuit=cuit,direccion=direccion)
            cliente.save()
            formulario_cliente=ClienteForm()
            return render(request,"clientes.html", {"mensaje":"Cliente Grabado", "formulario":formulario_cliente})
        return render(request,"clientes.html", {"mensaje":"Datos Invalidos"})
    else:
        formulario_cliente=ClienteForm()
    clientes = Cliente.objects.all()
    return render(request,"clientes.html", {"formulario": formulario_cliente, "clientes":clientes})




def articulos(request):
    if request.method == "POST":
        form=ArticuloForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            descripcion=info["descripcion"]
            marca=info["marca"]
            articulo=Articulo(descripcion=descripcion,marca=marca)
            articulo.save()
            formulario_articulo=ArticuloForm()
            return render(request,"articulos.html", {"mensaje":"Articulo Grabado", "formulario":formulario_articulo})
        return render(request,"articulos.html", {"mensaje":"Datos Invalidos"})
    else:
        formulario_articulo=ArticuloForm()
        articulos =Articulo.objects.all()
    return render(request,"articulos.html", {"formulario": formulario_articulo, "articulos":articulos})

def provedores(request):
    if request.method == "POST":
        form=ProvedorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            cuit=info["cuit"]
            direccion=info["direccion"]
            provedor=Provedor(nombre=nombre,cuit=cuit,direccion=direccion)
            provedor.save()
            formulario_provedor=ProvedorForm()
            return render(request,"provedores.html", {"mensaje":"Provedor Grabado", "formulario":formulario_provedor})
        return render(request,"provedores.html", {"mensaje":"Datos Invalidos"})
    else:
        formulario_provedor=ProvedorForm()
        provedores =Provedor.objects.all()
    return render(request,"provedores.html", {"formulario": formulario_provedor, "provedores":provedores})
        



def compras(request):
    if request.method == "POST":
        form=ComprasForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            fecha=info["fecha"]
            provedor=info["provedor"]
            nfactura=info["nfactura"]
            importe=info["importe"]
            compra=Compras(fecha=fecha,provedor=provedor,nfactura=nfactura,importe=importe)
            compra.save()
            formulario_compras=ComprasForm()
            return render(request,"compras.html", {"mensaje":"Compra Grabada", "formulario": formulario_compras})
        return render(request,"compras.html", {"mensaje":"Datos Invalidos"})
    else:
        formulario_compras=ComprasForm()
        compras =Compras.objects.all()
    return render(request,"compras.html", {"formulario": formulario_compras,"compras":compras})
        

def busquedacliente(request):
    return render(request,"busquedacliente.html")
    
def buscar(request):
    nombre=request.GET["nombre"]
    if nombre!="":
        clientes=Cliente.objects.filter(nombre__icontains=nombre)
        return render(request,"resultadosbusqueda.html",{"clientes":clientes})
    else:
        return render(request, "busquedacliente.html",{"mensaje": "No se ha Ingresado ningun dato"})

def listadodeclientes(request):
    cliente = Cliente.objects.all()
    respuesta=""
    for cliente in clientes:
        respuesta+=f"{cliente.nombre} - {cliente.cuit} - {cliente.direccion} <br>"
    return HttpResponse(respuesta)

def listarclientes(request):
    clientes = Cliente.objects.all()    
    return render(request,"listarclientes.html",{"clientes":clientes})

