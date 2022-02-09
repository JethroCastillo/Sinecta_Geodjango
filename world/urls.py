from django.urls import path
from .views import PredioApi

urlpatterns = [
    path('predio/', PredioApi, name='predio_list'),
    
]