from django.urls import path
from . import views

urlpatterns=[
    path('categoria',views.categoria_list,name='categoria_list'),
    path('categoria/nuevo',views.categoria_nuevo, name="categoria_nuevo"),
    path('categoria/<int:pk>/editar/', views.categoria_editar, name='categoria_editar'),
    path('categoria/<int:pk>/eliminar/', views.categoria_eliminar, name='categoria_eliminar')
]