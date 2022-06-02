from django.http import HttpResponse
from Ventas.models import Sardo, Regg, Prov
from django.shortcuts import render
from django.template import loader

def producto(self):

    sardo = Sardo(producto = 'Sardo', calidad = ['Duro', 'Semi'], precio = [1500, 1600])
    sardo.save()

    reggiano = Regg(producto = 'Reggiano', calidad = 'Duro', precio = 2000)
    reggiano.save()

    provolone = Prov(producto = 'Provolone', calidad = 'Duro', precio = 1800)
    provolone.save()

    
    portal = f'Nuestros productos: {sardo.nombre} {reggiano.nombre} {provolone.nombre} en calidad de: {sardo.calidad} {reggiano.calidad} {provolone.calidad} a precio: {sardo.precio} {reggiano.precio} {provolone.precio}'
    return HttpResponse(portal)

def miportal(request):

    plantilla = loader.get_template('portal.html')
    portal =plantilla.render()

    return HttpResponse(portal)
