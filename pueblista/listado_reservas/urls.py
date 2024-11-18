from django.urls import path
from listado_reservas import views

urlpatterns = [
    path('', views.listado_reservas, name='listado_reservas'),
    path('eliminar_reserva/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),
    path('modificar_reserva/<int:reserva_id>/', views.modificar_reserva, name='modificar_reserva'),
]