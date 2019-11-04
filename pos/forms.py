from django import forms
from .models import Categoria,Producto,Cliente

class CategoriaForm(forms.ModelForm):
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class':'form-text'}))
    class Meta:
        model=Categoria
        fields=("nombre",)

class ProductoForm(forms.ModelForm):
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class':'form-text'}))
    precio_venta=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-text'}))
    precio_compra=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-text'}))
    existencia=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-text'}))
    # categoria=forms.ModelMultipleChoiceField(widget=forms.Select(attrs={'class':'form-text'}),queryset=Categoria.objects.all())
    class Meta:
        model=Producto
        fields=("nombre","precio_venta","precio_compra","existencia","categoria",)

class ClienteForm(forms.ModelForm):
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class':'form-text'}))
    apellido=forms.CharField(widget=forms.TextInput(attrs={'class':'form-text'}))
    telefono=forms.CharField(widget=forms.TextInput(attrs={'class':'form-text mask-phone'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-text'}))
    direccion=forms.CharField(widget=forms.TextInput(attrs={'class':'form-text'}))
    class Meta:
        model=Cliente
        fields=("nombre","apellido","telefono","email","direccion",)
    