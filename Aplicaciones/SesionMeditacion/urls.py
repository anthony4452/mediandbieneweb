from django.urls import path
from . import views

urlpatterns = [
    path('sesiones/calendario/', views.calendario_sesiones, name='calendario_sesiones'),
    path('sesiones/api/', views.sesiones_api, name='sesiones_api'),
    path('sesiones/', views.sesiones_list, name='sesiones_list'),

    path('sesiones/nuevo/', views.nuevaSesion, name='nuevo_sesion'),
    path('sesiones/guardar/', views.guardarSesion, name='guardar_sesion'),
    path('sesiones/editar/<int:id>/', views.editarSesion, name='editar_sesion'),
    path('sesiones/guardarEdicion/<int:id>/', views.guardarEdicionSesion, name='guardar_edicion_sesion'),
    path('sesiones/eliminar/<int:id>/', views.eliminarSesion, name='eliminar_sesion'),
]
