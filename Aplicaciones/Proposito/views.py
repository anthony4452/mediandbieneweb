from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Proposito
from django.contrib.auth.decorators import login_required, user_passes_test
from Aplicaciones.SesionMeditacion.models import SesionMeditacion  

def es_admin(user):
    return user.is_staff or (hasattr(user, 'perfilusuario') and user.perfilusuario.rol.upper() in ['ADMIN', 'ADMINISTRADOR'])

@login_required
@user_passes_test(es_admin)
def propositos(request):
    propositos = Proposito.objects.all().order_by('-created_at')
    return render(request, 'propositos.html', {'propositos': propositos})

@login_required
@user_passes_test(es_admin)
def nuevoProposito(request):
    return render(request, 'nuevoProposito.html')

@login_required
@user_passes_test(es_admin)
def guardarProposito(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        categoria = request.POST.get("categoria")
        activo = request.POST.get("activo") == "on"  # checkbox

        # Aquí podrías agregar validaciones manuales si quieres

        Proposito.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            categoria=categoria,
            activo=activo,
        )

        messages.success(request, "Se ha guardado el propósito correctamente")
        return redirect('propositos')
    else:
        return redirect('nuevoProposito/')

@login_required
@user_passes_test(es_admin)
def editarProposito(request, id):
    proposito = get_object_or_404(Proposito, pk=id)

    categorias = [
        "Salud",
        "Trabajo",
        "Espiritualidad",
        "Educación",
        "Relaciones",
    ]

    return render(request, 'editarProposito.html', {
        'proposito': proposito,
        'categorias': categorias,
    })


@login_required
@user_passes_test(es_admin)
def guardarEdicionProposito(request, id):
    if request.method == "POST":
        proposito = get_object_or_404(Proposito, pk=id)

        proposito.nombre = request.POST.get("nombre")
        proposito.descripcion = request.POST.get("descripcion")
        proposito.categoria = request.POST.get("categoria")
        proposito.activo = request.POST.get("activo") == "on"

        proposito.save()

        messages.success(request, "Propósito actualizado correctamente")
        return redirect('propositos')
    else:
        return redirect('propositos')

@login_required
@user_passes_test(es_admin)
def eliminarProposito(request, id):
    proposito = get_object_or_404(Proposito, pk=id)

    # Verifica si el propósito está relacionado con alguna sesión
    if SesionMeditacion.objects.filter(proposito=proposito).exists():
        messages.error(request, "No se puede eliminar el propósito porque está en uso en sesiones de meditación.")
        return redirect('propositos')

    # Si no está relacionado, se puede eliminar
    proposito.delete()
    messages.success(request, "Propósito eliminado correctamente")
    return redirect('propositos')