from django import forms


class ComprasForm(forms.Form):
    fecha=forms.DateField()
    nfactura=forms.CharField(max_length=15)
    provedor=forms.CharField(max_length=40)
    importe=forms.DecimalField(max_digits=20, decimal_places=2)        

class ClienteForm(forms.Form):
    nombre=forms.CharField(max_length=40)
    cuit=forms.IntegerField()
    direccion=forms.CharField(max_length=40)

class ProvedorForm(forms.Form):
    nombre=forms.CharField(max_length=40)
    cuit=forms.IntegerField()
    direccion=forms.CharField(max_length=40) 


class ArticuloForm(forms.Form):
    descripcion =forms.CharField(max_length=50)
    marca =forms.CharField(max_length=40)    
