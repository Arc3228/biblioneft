from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .models import Book


# Регистрируем модель User с кастомным админ-классом
admin.site.register(User)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn', 'added_by', 'borrowed_by')
    list_filter = ('author', 'published_date', 'added_by', 'borrowed_by')
    search_fields = ('title', 'author', 'isbn')
    date_hierarchy = 'published_date'