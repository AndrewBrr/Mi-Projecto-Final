from django.urls import path 
from Ventas import views
from Ventas.views import miportal, sardo, reggiano, provolone, sardo_formulario, regg_formulario, prov_formulario
from Ventas.forms import formulario_S

urlpatterns = [

    path('portal/', miportal, name='Portal'),   
    path('sardo/',sardo, name='Sardo'), 
    path('reggiano/', reggiano, name='Reggiano'),
    path('provolone/', provolone, name='Provolone'),
    path('sardo_formulario/', sardo_formulario,name='sardo_formulario'),
    path('regg_formulario/', regg_formulario,name='regg_formulario'),
    path('prov_formulario/', prov_formulario,name='prov_formulario'),


]
