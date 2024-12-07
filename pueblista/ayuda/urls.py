from django.urls import path
from ayuda import views

urlpatterns = [
    path('', views.ayuda, name='ayuda'),
]
