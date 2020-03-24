from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('add/form_productos/', views.form_productos),
    path('add/', views.alta_productos),
    path('find/fbp/', views.form_buscar_productos),
    path('find/', views.buscar_productos),
    path('delete/fep/del/', views.eliminar_producto),
    path('delete/fep/', views.form_buscar_productos_eliminar),
    path('delete/', views.buscar_eliminar_productos),
    path('modify/', views.modificar_producto),
    path('', views.productos),


]
