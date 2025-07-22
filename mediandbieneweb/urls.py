from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('Aplicaciones.Usuarios.urls')), 
    path('propositos/', include('Aplicaciones.Proposito.urls')),
    path('sesiones/', include('Aplicaciones.SesionMeditacion.urls')),
    path('mensajes/', include('Aplicaciones.Mensajes.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)