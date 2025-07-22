from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib import messages
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya está en uso')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1, rol='USUARIO')
        messages.success(request, 'Cuenta creada correctamente. Inicia sesión.')
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.rol == 'ADMINISTRADOR':
                return redirect('admin_dashboard')
            else:
                return redirect('usuario_dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')

    return render(request, 'login.html')

@login_required
def admin_dashboard(request):
    if request.user.rol != 'ADMINISTRADOR':
        return HttpResponseForbidden("No tienes permiso.")
    return render(request, 'dashboards/admin_dashboard.html')


@login_required
def usuario_dashboard(request):
    if request.user.rol != 'USUARIO':
        return HttpResponseForbidden("No tienes permiso.")
    return render(request, 'dashboards/usuario_dashboard.html')
