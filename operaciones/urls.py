from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('add/form_operaciones/', views.form_operaciones),
    path('add/', views.alta_operaciones),
    path('find/fbp/', views.form_buscar_operaciones),
    path('find/', views.buscar_operaciones),
    path('delete/fep/del/', views.eliminar_operacion),
    path('delete/fep/', views.form_buscar_operaciones_eliminar),
    path('delete/', views.buscar_eliminar_operaciones),
    path('', views.operaciones),

]
