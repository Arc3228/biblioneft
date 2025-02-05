# Generated by Django 3.2.25 on 2025-02-06 14:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название мероприятия')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('event_type', models.CharField(choices=[('concert', 'Концерт'), ('lecture', 'Лекция'), ('workshop', 'Мастер-класс'), ('meetup', 'Встреча'), ('other', 'Другое')], max_length=50, verbose_name='Тип мероприятия')),
                ('start_date', models.DateTimeField(verbose_name='Дата и время начала')),
                ('location', models.CharField(max_length=200, verbose_name='Место проведения')),
                ('max_participants', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Максимальное количество участников')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('organizer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organized_events', to=settings.AUTH_USER_MODEL, verbose_name='Организатор')),
                ('participants', models.ManyToManyField(blank=True, related_name='events_participated', to=settings.AUTH_USER_MODEL, verbose_name='Участники')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]
