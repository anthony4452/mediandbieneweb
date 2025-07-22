from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('Aplicaciones.Usuarios.urls')), 
    path('proposito/', include('Aplicaciones.Proposito.urls')),
    path('sesiones/', include('Aplicaciones.SesionMeditacion.urls')),
]
