# Generated by Django 5.1.6 on 2025-02-13 07:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_borrowedbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbook',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books_book', to='main.book', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='borrowedbook',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
