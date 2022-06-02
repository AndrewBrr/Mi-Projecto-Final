from unittest.util import _MAX_LENGTH
from django.db import models

class Sardo(models.Model):

    producto = models.CharField(max_length=10)
    calidad = models.CharField(max_length=10)
    precio = models.IntegerField()

class Regg(models.Model):

    producto = models.CharField(max_length=10)
    calidad = models.CharField(max_length=10)
    precio = models.IntegerField()

class Prov(models.Model):

    producto = models.CharField(max_length=10)
    calidad = models.CharField(max_length=10)
    precio = models.IntegerField()


