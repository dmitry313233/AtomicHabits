from rest_framework import serializers

from habits.models import Habits
from habits.validators import exception, time_performance, grafted_habit, body_sign_pleasant_habit, period_habit


class HabitsSerializer(serializers.ModelSerializer):
    # url = serializers.URLField(validators=[exception()])

    class Meta:
        model = Habits
        fields = '__all__'
        validators = [exception, grafted_habit, body_sign_pleasant_habit]
