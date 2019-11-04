from django.urls import path
from . import views

urlpatterns=[
    path('',views.my_inicio,name='my_inicio'),
    # URL CATEGORIA
    path('categoria',views.categoria_list,name='categoria_list'),
    path('categoria/nuevo',views.categoria_nuevo, name="categoria_nuevo"),
    path('categoria/<int:pk>/editar/', views.categoria_editar, name='categoria_editar'),
    path('categoria/<int:pk>/eliminar/', views.categoria_eliminar, name='categoria_eliminar'),

    # URL PRODUCTOS
    path('producto',views.producto_list,name='producto_list'),
    path('producto/nuevo',views.producto_nuevo, name="producto_nuevo"),
    path('producto/<int:pk>/editar/', views.producto_editar, name='producto_editar'),
    path('producto/<int:pk>/eliminar/', views.producto_eliminar, name='producto_eliminar'),

    # URL CLIENTES
    path('cliente',views.cliente_list,name='cliente_list'),
    path('cliente/nuevo',views.cliente_nuevo, name="cliente_nuevo"),
    path('cliente/<int:pk>/editar/', views.cliente_editar, name='cliente_editar'),
    path('cliente/<int:pk>/eliminar/', views.cliente_eliminar, name='cliente_eliminar'),
    
    #URL VENTAS
    path('venta',views.venta_list,name='venta_list'),
    path('venta/nuevo',views.venta_list,name='venta_nuevo'),

]