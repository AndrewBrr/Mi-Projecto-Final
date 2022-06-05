from django import forms

class formulario_S(forms.Form):

    
    producto = forms.CharField(max_length=10)
    calidad = forms.CharField(max_length=10)
    precio = forms.IntegerField()

class formulario_R(forms.Form):

    producto = forms.CharField(max_length=10)
    calidad = forms.CharField(max_length=10)
    precio = forms.IntegerField()


class formulario_P(forms.Form):

    producto = forms.CharField(max_length=10)
    calidad = forms.CharField(max_length=10)
    precio = forms.IntegerField()
