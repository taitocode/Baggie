from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('add/form_empaques/', views.form_empaques),
    path('add/', views.alta_empaques),
    path('find/fbp/', views.form_buscar_empaques),
    path('find/', views.buscar_empaques),
    path('delete/fee/del/', views.eliminar_empaque),
    path('delete/fee/', views.form_buscar_empaques_eliminar),
    path('delete/', views.buscar_eliminar_empaques),
    path('modify/', views.modificar_empaque),
    path('', views.empaques),

]
