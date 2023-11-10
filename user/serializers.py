from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):

    # telegram = serializers.SerializerMethodField()
    #
    # def get_telegram(self, instance):
    #     """Для полноценной работы сервиса необходим реализовать работу с отложенными задачами
    #      для напоминания о том, в какое время какие привычки необходимо выполнять. """
    #     return send_message(instance.grafted_habit)  # Возвращаем метод в services, instance.grafted_habit обращаемся к Habits.grafted_habit

    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, value):
        return make_password(value)
