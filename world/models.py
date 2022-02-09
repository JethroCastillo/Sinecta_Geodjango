from django.contrib.gis.db import models

# Create your models here.

class Predio(models.Model):
    name = models.CharField(max_length=100)
    poly = models.PolygonField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=60) 

