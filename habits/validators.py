from django.core.exceptions import ValidationError


def exception(value):
    """Исключить одновременный выбор связанной привычки и указания вознаграждения."""
    if value.get('grafted_habit') and value.get('reward'):
        raise ValidationError('Вы не можете выбрать или приятную привычку или вознаграждение!')


def time_performance(value):
    """Время выполнения должно быть не больше 120 секунд."""
    if value.get('time_performance') > 120:
        raise ValidationError('Время выполнения больше 2 минут')


def grafted_habit(value):  # !!!!
    """В связанные привычки могут попадать только привычки с признаком приятной привычки."""
    if value.get('sign_pleasant_habit') and value.get('grafted_habit'):
        raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки!')


def body_sign_pleasant_habit(value):
    """У приятной привычки не может быть вознаграждения или связанной привычки."""
    if sum([bool(value.get('sign_pleasant_habit')), bool(value.get('grafted_habit')), bool(value.get('reward'))]) > 1:
        raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки!')


def period_habit(value):  # !!!!
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней."""
    if value.get('periodicity') > 7:
        raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней!')
