from datetime import datetime

from celery import shared_task
from telebot import TeleBot

from habits.models import Habits


@shared_task
def check_time_habit():
    datatime_now = datetime.now()
    time_now = datatime_now.strftime("%H:%M:00")
    habits = Habits.objects.filter(time=time_now)
    for habit in habits:
        if habit:
            bot = TeleBot("6977081448:AAEvZJAYEvt7UKfuT90tOA0mwyVYzDzH_PI")
            bot.send_message(947497532, 'skypro')  # Привязка к телеграмм боту