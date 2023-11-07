from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    telegram_name = models.CharField(max_length=50, verbose_name='telegram_name')
    user_telegram_id = models.CharField(max_length=40, verbose_name='user_telegram_id')
    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.telegram_name} {self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

