from django.urls import path
from gestion_reservas import views

urlpatterns = [
    path('', views.calendario_reservas, name='calendario_reservas'),
    path('crear/', views.crear_reserva, name='crear_reserva'),
    path('cancelar/<int:id>/', views.cancelar_reserva, name='cancelar_reserva'),
    path('solicitud-espacio/', views.solicitud_reserva_especial, name='solicitud_reserva_especial'),
    path('mis-solicitudes', views.mis_solicitudes, name='mis_solicitudes'),
    path('solicitudes-pendientes', views.solicitudes_pendientes, name='solicitudes_pendientes'),
    path('aceptar-solicitud', views.aceptar_solicitud, name='aceptar_solicitud'),
]
