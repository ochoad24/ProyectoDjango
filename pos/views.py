from django.shortcuts import render
from .models import Categoria
# Create your views here.
def categoria_list(request):
    categorias=Categoria.objects.filter()
    return render(request,'pos/categoria_list.html',{'categorias':categorias})
