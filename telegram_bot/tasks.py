import os
from datetime import datetime
import dotenv

from celery import shared_task
from telebot import TeleBot

from habits.models import Habits

dotenv.load_dotenv()   # Это для файла .env

@shared_task
def check_time_habit():
    datatime_now = datetime.now()
    time_now = datatime_now.strftime("%H:%M:00")
    habits = Habits.objects.filter(time=time_now)
    for habit in habits:
        if habit:
            bot = TeleBot(os.getenv('telegramapi_key'))
            #bot.send_message(947497532, 'skypro')  # Привязка к телеграмм боту
            bot.send_message(os.getenv('chat_id_telegram'), os.getenv('chat_name'))
