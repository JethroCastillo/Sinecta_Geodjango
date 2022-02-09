from django.urls import path
from .views import PredioApi, PredioDetailApi, delete_view

urlpatterns = [
    path('predio/', PredioApi, name='predio_list'),
    path('predio/<int:id>/', delete_view, name='predio_list'),
    
]