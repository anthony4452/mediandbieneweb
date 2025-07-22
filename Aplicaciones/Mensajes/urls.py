from django.urls import path
from . import views

urlpatterns = [
    path('', views.mensajes, name='mensajes'),
    path('guardarMensaje/', views.guardarMensaje, name='guardarMensaje'),
    path('enviar_mensaje/<int:id>/', views.enviar_mensaje, name='enviar_mensaje'),
    path('listarMensaje/', views.listarMensaje, name='listarMensaje'),
    path('listarMensaje/<int:id_editar>/', views.listarMensaje, name='editarMensaje'),
    path('eliminarMensaje/<int:id>/', views.eliminarMensaje, name='eliminarMensaje'),
]
