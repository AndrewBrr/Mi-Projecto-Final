from django.urls import path 
from Ventas import views
from Ventas.views import miportal, producto

urlpatterns = [

    path('producto/', producto),
    path('miportal/', miportal),    
]
