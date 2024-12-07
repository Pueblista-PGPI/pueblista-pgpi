from django.urls import path
from . import views

urlpatterns = [
    path('', views.mis_notificaciones, name='notificaciones'),
    path('marcar_leida/<int:notificacion_id>/', views.marcar_leida, name='marcar_leida'),
    path('eliminar/<int:notificacion_id>/', views.borrar_notificacion, name='borrar_notificacion'),
    path('eliminar-todas/', views.borrar_todas_leidas, name='borrar_todas_leidas'),
]
