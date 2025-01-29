from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# Регистрируем модель User с кастомным админ-классом
admin.site.register(User)