from django.urls import path
from gestion_espacios import views

urlpatterns = [
    path('', views.index, name='index'),
    
]