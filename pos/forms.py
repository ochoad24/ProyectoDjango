from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class':'form-text'}))
    class Meta:
        model=Categoria
        fields=("nombre",)

    
    