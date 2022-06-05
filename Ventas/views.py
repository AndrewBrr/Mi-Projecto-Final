from django.http import HttpResponse
from Ventas.models import Sardo, Reggiano, Provolone
from django.shortcuts import render
from django.template import loader
from Ventas.forms import formulario_S, formulario_R, formulario_P

def sardo(request):

    sardo = Sardo(producto = 'Sardo', calidad = 'Duro', precio = 1600)
    semi = Sardo(producto = 'Sardo Semi', calidad = 'Semi-Duro', precio = 1400)
    sardo.save()
    semi.save()

    info_sardo = f'El producto {sardo.producto}, que viene en calidad de {sardo.calidad} a precio de {sardo.precio}'
    return render(request, 'Ventas/sardo.html')

def reggiano(request):

    reggiano = Reggiano(producto = 'Reggiano', calidad = 'Duro', precio = 2000)
    reggiano.save()

    info_regg = f'El producto {reggiano.producto} solo viene en calidad de {reggiano.calidad} a precio de {reggiano.precio}'
    return render(request, 'Ventas/reggiano.html/')

def provolone(request):
    provolone = Provolone(producto = 'Provolone', calidad = 'Duro', precio = 1800)
    provolone.save()

    info_prov = f'El producto {provolone.producto} solo viene en calidad de {provolone.calidad} a precio de {provolone.precio}'
    return render(request, 'Ventas/provolone.html')
    
def miportal(self):

    plantilla = loader.get_template('Ventas/portal.html')
    portal = plantilla.render()
    return HttpResponse(portal)

def sardo_formulario(request):

    if request.method == 'POST':

        form_sardo = formulario_S(request.POST)

    
        if form_sardo.is_valid():

            info = form_sardo.cleaned_data
            producto = info['producto']
            calidad = info['calidad']
            precio = info['precio']

            sardo = Sardo(producto = producto, calidad = calidad, precio = precio)
            sardo.save()

        return render(request, 'Ventas/portal.html')

    else:
        form_sardo = formulario_S()

        return render(request, 'Ventas/sardo_formulario.html',  {'form_sardo':form_sardo})


def regg_formulario(request):
    
    
    if request.method == 'POST':

        form_regg = formulario_R(request.POST)

    
        if form_regg.is_valid():

            info = form_regg.cleaned_data
            producto = info['producto']
            calidad = info['calidad']
            precio = info['precio']

            reggiano = Reggiano(producto = producto, calidad = calidad, precio = precio)
            reggiano.save()

        return render(request, 'Ventas/portal.html')

    else:
        form_regg = formulario_R()

        return render(request, 'Ventas/regg_formulario.html',  {'form_regg':form_regg})


def prov_formulario(request):
    
    
    if request.method == 'POST':

        form_prov = formulario_P(request.POST)

    
        if form_prov.is_valid():

            info = form_prov.cleaned_data
            producto = info['producto']
            calidad = info['calidad']
            precio = info['precio']

            provolone = Provolone(producto = producto, calidad = calidad, precio = precio)
            provolone.save()

        return render(request, 'Ventas/portal.html')

    else:
        form_prov = formulario_P()

        return render(request, 'Ventas/prov_formulario.html',  {'form_prov':form_prov})
