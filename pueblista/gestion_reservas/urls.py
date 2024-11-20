from django.urls import path
from gestion_reservas import views

urlpatterns = [
    path('', views.calendario_reservas, name='calendario_reservas'),
    path('crear/', views.crear_reserva, name='crear_reserva'),
    path('cancelar/<int:id>/', views.cancelar_reserva, name='cancelar_reserva'),
    path('solicitud-espacio/', views.solicitud_reserva_especial, name='solicitud_reserva_especial'),
]
