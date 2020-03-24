from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('add/form_incidencias/', views.form_incidencias),
    path('add/', views.form_incidencias),
    path('find/fbp/', views.form_buscar_incidencias),
    path('find/', views.buscar_incidencias),
    path('delete/fep/del/', views.eliminar_incidencia),
    path('delete/fep/', views.form_buscar_incidencias_eliminar),
    path('delete/', views.buscar_eliminar_incidencias),
    path('modify/', views.modificar_incidencia),
    path('', views.incidencias),

]
