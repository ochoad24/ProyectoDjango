from django.shortcuts import render,get_object_or_404,redirect
from .models import Categoria,Producto,Cliente,Encabezado,Detalle
from .forms import CategoriaForm,ProductoForm,ClienteForm,EncabezadoForm,DetalleForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def my_inicio(request):
    return render(request,'pos/inicio.html')
# VISTAD DE CATEGORIA
@login_required
def categoria_list(request):
    categorias=Categoria.objects.all()
    return render(request,'pos/categoria_list.html',{'categorias':categorias})

@login_required    
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
    
@login_required
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

@login_required
def categoria_eliminar(request,pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if(request.method=="POST"):
        categoria.delete()
        return redirect('categoria_list')
    else:
        return render(request, 'pos/categoria_eliminar.html', {'categoria':categoria.nombre })

# CRUD PRODUCTOS
@login_required
def producto_list(request):
    productos=Producto.objects.all()
    return render(request,'pos/producto_list.html',{'productos':productos})
    
@login_required
def producto_nuevo(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'pos/producto.html', {'form': form})

@login_required
def producto_editar(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'pos/producto.html', {'form': form})

@login_required
def producto_eliminar(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    if(request.method=="POST"):
        producto.delete()
        return redirect('producto_list')
    else:
        return render(request, 'pos/producto_eliminar.html', {'producto':producto })

# CURS CLIENTES
@login_required
def cliente_list(request):
    clientes=Cliente.objects.all()
    return render(request,'pos/cliente_list.html',{'clientes':clientes})
    
@login_required
def cliente_nuevo(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'pos/cliente.html', {'form': form})

@login_required
def cliente_editar(request,pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'pos/cliente.html', {'form': form})

@login_required
def cliente_eliminar(request,pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if(request.method=="POST"):
        cliente.delete()
        return redirect('cliente_list')
    else:
        return render(request, 'pos/cliente_eliminar.html', {'cliente':cliente })

# VIEWS VENAS LISTA
@login_required
def venta_list(request):
    ventas=Encabezado.objects.all()
    return render(request,'pos/venta_list.html',{'ventas':ventas})

@login_required
def venta_nuevo(request):
    if request.method == "POST":
        # form = ClienteForm(request.POST)
        # if form.is_valid():
        #     cliente = form.save(commit=False)
        #     cliente.save()
        return redirect('cliente_list')
    else:
        form = EncabezadoForm()
        form2 = DetalleForm()
    return render(request, 'pos/venta.html', {'form': form,'form2':form2})