from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservas/', include('gestion_espacios.urls')),
    path('auth/', include('gestion_usuarios.urls')),
    path('contact/', include('gestion_contactos.urls')),
    path('', include('home.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
