from django.urls import path
from django.shortcuts import redirect
from gestion_usuarios import views

urlpatterns = [
    path('', lambda request: redirect('login/')),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'), 
    path('user_list/', views.user_list, name='user_list'),
]
