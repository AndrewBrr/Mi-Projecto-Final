from django.urls import path 
from Ventas import views
from Ventas.views import miportal, sardo, reggiano, provolone

urlpatterns = [

    path('portal/', miportal, name='Portal'),   
    path('sardo/',sardo, name='Sardo'), 
    path('reggiano/', reggiano, name='Reggiano'),
    path('provolone/', provolone, name='Provolone')

]
