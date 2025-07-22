from django.urls import path
from . import views

urlpatterns = [
    path('propositos/', views.propositos, name='propositos'),
    path('propositos/nuevoProposito/', views.nuevoProposito, name='nuevo_proposito'),
    path('propositos/guardarProposito/', views.guardarProposito, name='guardar_proposito'),
    path('propositos/editarProposito/<int:id>/', views.editarProposito, name='editar_proposito'),
    path('propositos/guardarEdicionProposito/<int:id>/', views.guardarEdicionProposito, name='guardar_edicion_proposito'),
    path('propositos/eliminarProposito/<int:id>/', views.eliminarProposito, name='eliminar_proposito'),
]
