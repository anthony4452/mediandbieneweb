from django.urls import path
from . import views

urlpatterns = [
    path('calendario/', views.calendario_sesiones, name='calendario_sesiones'),
    path('api/', views.sesiones_api, name='sesiones_api'),
    path('', views.sesiones_list, name='sesiones_list'),
    path('nuevo/', views.nuevaSesion, name='nuevo_sesion'),
    path('guardar/', views.guardarSesion, name='guardar_sesion'),
    path('editar/<int:id>/', views.editarSesion, name='editar_sesion'),
    path('guardarEdicion/<int:id>/', views.guardarEdicionSesion, name='guardar_edicion_sesion'),
    path('eliminar/<int:id>/', views.eliminarSesion, name='eliminar_sesion'),
]
