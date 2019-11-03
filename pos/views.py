from django.shortcuts import render,get_object_or_404,redirect
from .models import Categoria
from .forms import CategoriaForm
# Create your views here.
def categoria_list(request):
    categorias=Categoria.objects.all()
    return render(request,'pos/categoria_list.html',{'categorias':categorias})
    
def categoria_nuevo(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'pos/categoria.html', {'form': form})
def categoria_editar(request,pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'pos/categoria.html', {'form': form})

def categoria_eliminar(request,pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if(request.method=="POST"):
        categoria.delete()
        return redirect('categoria_list')
    else:
        return render(request, 'pos/categoria_eliminar.html', {'categoria':categoria.nombre })