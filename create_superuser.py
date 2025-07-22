import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mediandbieneweb.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.getenv("DJANGO_SUPERUSER_USERNAME", "Anthony")
email = os.getenv("DJANGO_SUPERUSER_EMAIL", "insanthoo@gmail.com")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "anthony23")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("✅ Superusuario creado automáticamente")
else:
    print("⚠️ El superusuario ya existe")
