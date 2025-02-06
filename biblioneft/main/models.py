from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The Phone field must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone, password, **extra_fields)


class User(AbstractBaseUser):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    education = models.CharField(max_length=100)
    prof = models.CharField(max_length=100)
    study_work = models.CharField(max_length=100)
    phone = models.CharField(max_length=18, unique=True)
    passport = models.CharField(max_length=11, unique=True)
    given = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name', 'surname', 'lastname', 'date_of_birth', 'education', 'prof', 'study_work', 'passport', 'given']
    objects = UserManager()

    def __str__(self):
        return f"{self.surname} {self.name}"

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    published_date = models.DateField(verbose_name="Дата публикации")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    pages = models.PositiveIntegerField(verbose_name="Количество страниц", validators=[MinValueValidator(1)])
    rating = models.FloatField(
        verbose_name="Рейтинг",
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        blank=True,
        null=True
    )
    added_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Добавлено пользователем",
        related_name="added_books"
    )
    borrowed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Взято на чтение",
        related_name="borrowed_books"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Event(models.Model):
    EVENT_TYPES = [
        ('concert', 'Концерт'),
        ('lecture', 'Лекция'),
        ('workshop', 'Мастер-класс'),
        ('meetup', 'Встреча'),
        ('other', 'Другое'),
    ]

    title = models.CharField(max_length=200, verbose_name="Название мероприятия")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES, verbose_name="Тип мероприятия")
    start_date = models.DateTimeField(verbose_name="Дата и время начала")
    location = models.CharField(max_length=200, verbose_name="Место проведения")
    organizer = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Организатор",
        related_name="organized_events"
    )
    participants = models.ManyToManyField(
        'User',
        related_name="events_participated",
        blank=True,
        verbose_name="Участники"
    )
    max_participants = models.PositiveIntegerField(
        verbose_name="Максимальное количество участников",
        validators=[MinValueValidator(1)],
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"{self.title} ({self.get_event_type_display()})"

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"