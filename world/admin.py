import imp
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Predio

# Register your models here.

# Testing the models with djangogis admin 
@admin.register(Predio)
class PredioAdmin(OSMGeoAdmin):
    list_display = ('name', 'poly')