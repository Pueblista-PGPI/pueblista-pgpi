from django.urls import path
from gestion_espacios import views

urlpatterns = [
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
    # path('reservas/<int:id>/', views.reservas, name='reservas'),
    path('reservas_fecha/<int:id>/', views.reservas, name='reservas_fecha'),
]
