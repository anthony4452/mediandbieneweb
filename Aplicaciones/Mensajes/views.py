from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils import timezone
import mimetypes

from .models import Mensaje

# LISTADO Y FORMULARIO (GET y POST en uno solo)
def listarMensaje(request, id_editar=None):
    if request.method == 'POST':
        id_mensaje = request.POST.get('id_mensaje')
        archivo = request.FILES.get('archivo')
        factura = request.FILES.get('factura')

        if id_mensaje:
            mensaje = get_object_or_404(Mensaje, pk=id_mensaje)
        else:
            mensaje = Mensaje()

        mensaje.titulo = request.POST.get('titulo')
        mensaje.destinatario = request.POST.get('destinatario')
        mensaje.asunto = request.POST.get('asunto')
        mensaje.mensaje = request.POST.get('mensaje')

        if archivo:
            mensaje.archivo = archivo
        if factura:
            mensaje.factura = factura

        mensaje.fecha = timezone.now()
        mensaje.save()

        messages.success(request, "Mensaje guardado correctamente")
        return redirect('/mensajes')

    mensajes = Mensaje.objects.all()
    mensaje_editar = get_object_or_404(Mensaje, pk=id_editar) if id_editar else None
    return render(request, 'listadoMensaje.html', {
        'mensajes': mensajes,
        'mensaje_editar': mensaje_editar
    })


# GUARDADO SIMPLE (si usas este desde otro formulario específico)
def guardarMensaje(request):
    if request.method == 'POST':
        Mensaje.objects.create(
            titulo=request.POST['titulo'],
            destinatario=request.POST['destinatario'],
            asunto=request.POST['asunto'],
            mensaje=request.POST['mensaje'],
            archivo=request.FILES.get('archivo'),
            factura=request.FILES.get('factura'),
            fecha=timezone.now()
        )
        messages.success(request, "Mensaje guardado exitosamente")
        return redirect('/mensajes')


# ENVÍO DE MENSAJE CON ADJUNTOS
def enviar_mensaje(request, id):
    mensaje = get_object_or_404(Mensaje, id=id)

    email = EmailMessage(
        subject=mensaje.asunto,
        body=mensaje.mensaje,
        from_email=settings.EMAIL_HOST_USER,
        to=[mensaje.destinatario],
    )

    if mensaje.archivo:
        file_type, _ = mimetypes.guess_type(mensaje.archivo.name)
        email.attach(mensaje.archivo.name, mensaje.archivo.read(), file_type)

    if mensaje.factura:
        factura_type, _ = mimetypes.guess_type(mensaje.factura.name)
        email.attach(mensaje.factura.name, mensaje.factura.read(), factura_type)

    email.send(fail_silently=False)
    messages.success(request, "Correo enviado correctamente")
    return redirect('/mensajes')


# ELIMINAR

def eliminarMensaje(request, id):
    Mensaje.objects.get(id=id).delete()
    messages.success(request, "Mensaje eliminado exitosamente")
    return redirect('/mensajes')


# CARGA SIMPLE DE LISTA

def mensajes(request):
    mensajes = Mensaje.objects.all()
    return render(request, 'listadoMensaje.html', {'mensajes': mensajes})
