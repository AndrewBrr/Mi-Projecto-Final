from django.urls import path 
from Ventas import views
from Ventas.views import miportal, sardo, reggiano, provolone

urlpatterns = [

    path('portal/', miportal),   
    path('sardo/',sardo,), 
    path('reggiano/', reggiano,),
    path('provolone/', provolone)

]
