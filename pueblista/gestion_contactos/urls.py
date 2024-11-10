from django.urls import path
from gestion_contactos import views

urlpatterns = [
    path('mail', views.contact_mail, name='contact_mail'),
    
]