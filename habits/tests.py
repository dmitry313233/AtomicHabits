from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits
from user.models import User


# Create your tests here.


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            telegram_name='user',
            user_telegram_id='1',
            email='user@mail.ru'
        )

        self.habits = Habits.objects.create(
            place='earth',
            action='eat',
            user=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_habits_create(self):
        data = {'place': self.habits.place, 'action': self.habits.action, 'user': self.user.pk}
        response = self.client.post(
            reverse('habits:habits_create'), data=data
        )

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

    def test_habits_list(self):
        response = self.client.get(
            reverse('habits:habits_list')
        )

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertTrue(
            Habits.objects.all().exists()
        )

    # def test_habits_retrieve(self):
    #     response = self.client.get(
    #         reverse('habits:habits_retrieve', args=[self.habits.pk])  # Обратить внимание на user.pk !!
    #     )
    #
    #     self.assertEqual(
    #         response.status_code, status.HTTP_200_OK
    #     )
    #
    # def test_habits_update(self):
    #     update_data = {'place': self.habits.place, 'action': self.habits.action, 'user': self.user.pk}
    #     response = self.client.put(
    #         reverse('habits:habits_update', args=[self.habits.pk]),  # Обратить внимание на user.pk !!
    #                 data=update_data
    #                 )
    #
    #     self.assertEqual(
    #         response.status_code, status.HTTP_200_OK
    #     )

    def test_habit(self):
        update_data = {'place': self.habits.place, 'action': self.habits.action, 'user': self.user.pk}
        response = self.client.put(
            reverse('habits:habit', args=[self.habits.pk]),  # Обратить внимание на user.pk !!
                    data=update_data
                    )

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
