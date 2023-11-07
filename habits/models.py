from datetime import timedelta

from django.db import models

from user.models import User

NULLABLE = {'blank': True, 'null': True}


class Habits(models.Model):
    place = models.CharField(max_length=30, verbose_name='место')
    time = models.TimeField(verbose_name='Время', **NULLABLE)
    action = models.CharField(max_length=70, verbose_name='действие')
    sign_pleasant_habit = models.BooleanField(default=False, verbose_name='признак приятной привычки', **NULLABLE)
    periodicity = models.DurationField(default=timedelta(days=1), verbose_name='периодичность')  # !!!!
    reward = models.CharField(max_length=100, verbose_name='вознаграждение', **NULLABLE)
    time_performance = models.DurationField(default=timedelta(seconds=120), verbose_name='время на выполнение',
                                            **NULLABLE)  # !!!!!
    sign_publicity = models.BooleanField(default=False, verbose_name='признак публичности', **NULLABLE)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    grafted_habit = models.ForeignKey('Habits', on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)
    # В связанные привычки могут попадать только привычки с признаком приятной привычки

    def __str__(self):
        return f'{self.user} {self.place} {self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
