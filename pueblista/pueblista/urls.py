from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('espacios/', include('gestion_espacios.urls')),
    path('espacios/<int:id>/reservas/', include('gestion_reservas.urls')),
    path('auth/', include('gestion_usuarios.urls')),
    path('mis_reservas/', include('listado_reservas.urls')),
    path('', include('home.urls')),
    path('notificaciones/', include('gestion_notificaciones.urls')),
    path('ayuda/', include('ayuda.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
