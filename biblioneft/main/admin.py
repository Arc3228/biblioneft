from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Event, Book, Role, BorrowedBook

# Регистрируем модель User с кастомным админ-классом
admin.site.register(User)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn', 'added_by', 'borrowed_by', 'file_book')
    list_filter = ('author', 'published_date', 'added_by', 'borrowed_by')
    search_fields = ('title', 'author', 'isbn')
    date_hierarchy = 'published_date'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'event_type', 'start_date', 'location', 'organizer', 'max_participants', 'created_at', 'updated_at')
    list_filter = ('event_type', 'location', 'is_active', 'max_participants')
    search_fields = ('title', 'event_type', 'organizer')


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrowed_date', 'returned_date', 'is_returned')
    list_filter = ('is_returned',)
    search_fields = ('user__name', 'book__title')