from django.http import HttpResponse
from Ventas.models import Sardo, Reggiano, Provolone
from django.shortcuts import render
from django.template import loader

def sardo(self):

    sardo = Sardo(producto = 'Sardo', calidad = 'Duro', precio = 1600)
    semi = Sardo(producto = 'Sardo Semi', calidad = 'Semi-Duro', precio = 1400)
    sardo.save()
    semi.save()

    info_sardo = f'El producto {sardo.producto}, que viene en calidad de {sardo.calidad} a precio de {sardo.precio}'
    return HttpResponse(info_sardo)

def reggiano(self):

    reggiano = Reggiano(producto = 'Reggiano', calidad = 'Duro', precio = 2000)
    reggiano.save()

    info_regg = f'El producto {reggiano.producto} solo viene en calidad de {reggiano.calidad} a precio de {reggiano.precio}'
    return HttpResponse(info_regg)

def provolone(self):
    provolone = Provolone(producto = 'Provolone', calidad = 'Duro', precio = 1800)
    provolone.save()

    info_prov = f'El producto {provolone.producto} solo viene en calidad de {provolone.calidad} a precio de {provolone.precio}'
    return HttpResponse(info_prov)
    
def miportal(request):

    plantilla = loader.get_template('portal.html')
    portal =plantilla.render()

    return HttpResponse(portal)
