from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import SesionMeditacion
from Aplicaciones.Proposito.models import Proposito
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date

User = get_user_model()

@login_required
def calendario_sesiones(request):
    # Vista que muestra el calendario y lista para admin y usuario
    return render(request, 'calendario_sesiones.html')

@login_required
def sesiones_api(request):
    # API para que fullcalendar pida las sesiones en JSON
    user = request.user
    if user.is_staff or (hasattr(user, 'perfilusuario') and user.perfilusuario.rol == 'admin'):
        sesiones = SesionMeditacion.objects.all()
    else:
        sesiones = SesionMeditacion.objects.filter(usuario=user)
    
    eventos = []
    for ses in sesiones:
        eventos.append({
            'id': ses.id,
            'title': f"{ses.proposito.nombre if ses.proposito else 'Sin propósito'} - {ses.calificacion}/10",
            'start': ses.fecha.isoformat(),
            'duration': ses.duracion_minutos,
            'allDay': True,
            'color': '#4caf50' if ses.calificacion >= 7 else '#f44336',
        })
    return JsonResponse(eventos, safe=False)

@login_required
def sesiones_list(request):
    # Listado simple tipo tabla para CRUD (opcional)
    sesiones = SesionMeditacion.objects.filter(usuario=request.user)
    return render(request, 'sesiones_list.html', {'sesiones': sesiones})

@login_required
def nuevaSesion(request):
    propositos = Proposito.objects.filter(activo=True).order_by('nombre')
    return render(request, 'nuevoSesion.html', {'propositos': propositos})

@login_required
def guardarSesion(request):
    if request.method == "POST":
        usuario = request.user
        proposito_id = request.POST.get('proposito')
        fecha = request.POST.get('fecha')
        duracion = request.POST.get('duracion_minutos')
        calificacion = request.POST.get('calificacion')

        proposito = None
        if proposito_id:
            proposito = get_object_or_404(Proposito, pk=proposito_id)

        # Validaciones básicas
        if not fecha or not duracion or not calificacion:
            messages.error(request, "Por favor complete todos los campos obligatorios")
            return redirect('nuevo_sesion')

        try:
            duracion = int(duracion)
            calificacion = int(calificacion)
        except ValueError:
            messages.error(request, "Duración y calificación deben ser números válidos")
            return redirect('nuevo_sesion')

        SesionMeditacion.objects.create(
            usuario=usuario,
            proposito=proposito,
            fecha=fecha,
            duracion_minutos=duracion,
            calificacion=calificacion
        )
        messages.success(request, "Sesión guardada correctamente")
        return redirect('calendario_sesiones')
    else:
        return redirect('nuevo_sesion')

@login_required
def editarSesion(request, id):
    sesion = get_object_or_404(SesionMeditacion, pk=id, usuario=request.user)
    propositos = Proposito.objects.filter(activo=True).order_by('nombre')
    return render(request, 'editarSesion.html', {'sesion': sesion, 'propositos': propositos})

@login_required
def guardarEdicionSesion(request, id):
    if request.method == "POST":
        sesion = get_object_or_404(SesionMeditacion, pk=id, usuario=request.user)

        proposito_id = request.POST.get('proposito')
        fecha = request.POST.get('fecha')
        duracion = request.POST.get('duracion_minutos')
        calificacion = request.POST.get('calificacion')

        proposito = None
        if proposito_id:
            proposito = get_object_or_404(Proposito, pk=proposito_id)

        if not fecha or not duracion or not calificacion:
            messages.error(request, "Por favor complete todos los campos obligatorios")
            return redirect('editar_sesion', id=id)

        try:
            duracion = int(duracion)
            calificacion = int(calificacion)
        except ValueError:
            messages.error(request, "Duración y calificación deben ser números válidos")
            return redirect('editar_sesion', id=id)

        sesion.proposito = proposito
        sesion.fecha = fecha
        sesion.duracion_minutos = duracion
        sesion.calificacion = calificacion
        sesion.save()

        messages.success(request, "Sesión actualizada correctamente")
        return redirect('calendario_sesiones')
    else:
        return redirect('calendario_sesiones')

@login_required
def eliminarSesion(request, id):
    sesion = get_object_or_404(SesionMeditacion, pk=id, usuario=request.user)
    sesion.delete()
    messages.success(request, "Sesión eliminada correctamente")
    return redirect('calendario_sesiones')
