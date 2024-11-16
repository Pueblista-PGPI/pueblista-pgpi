from django.urls import path
from gestion_reservas import views

urlpatterns = [
    # path('delete/<int:id>/', views.delete, name='delete'),
    # path('edit/<int:id>/', views.edit, name='edit'),
    path('', views.calendario_reservas, name='calendario_reservas'),
    path('crear/', views.crear_reserva, name='crear_reserva'),
    # path('create/', views.create, name='create'),
]
