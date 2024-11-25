from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit_ayuntamiento_info/<int:id>/', views.edit_ayuntamiento_info, name='edit_ayuntamiento_info'),
    path('add_ayuntamiento_info/', views.add_ayuntamiento_info, name='add_ayuntamiento_info'),
]
