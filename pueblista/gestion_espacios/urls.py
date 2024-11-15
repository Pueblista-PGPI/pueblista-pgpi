from django.urls import path
from gestion_espacios import views

urlpatterns = [
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
]
