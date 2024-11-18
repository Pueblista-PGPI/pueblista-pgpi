from django.urls import path
from listado_reservas import views

urlpatterns = [
    path('', views.listado_reservas, name='listado_reservas'),
]