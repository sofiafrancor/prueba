from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	path('registro/', views.registrar, name="registrar"),
    path('empresas/', views.empresas, name="empresa"),
    path('empresas/<int:pk>/', views.empresasEdit, name="empresasEdit"),

]