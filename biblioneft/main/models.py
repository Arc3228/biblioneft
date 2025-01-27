from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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
    phone = models.CharField(max_length=20, unique=True)
    passport = models.CharField(max_length=11)
    given = models.CharField(max_length=100)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name', 'surname', 'lastname', 'date_of_birth', 'education', 'prof', 'study_work', 'passport', 'given']
    objects = UserManager()