from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('editar/ayuntamiento/', views.editar_ayuntamiento, name='editar_ayuntamiento'),
]
