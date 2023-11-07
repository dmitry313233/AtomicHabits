from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.paginators import HabitsPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitsSerializer


class HabitsCreateListAPIView(generics.ListCreateAPIView):
    """Создание привычки"""
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]
    queryset = Habits.objects.all()
    # def form_valid(self, form):   # Это для Django
    #     user = self.request.user
    #     self.object = form.save()
    #     self.object.user = user
    #     self.object.save()
    #     return super().form_valid(form)   # !!!!

    def perform_create(self, serializer):  # Для сохранения владельца при создании привычки
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()

    def get_queryset(self):
        """
            Getting Lesson Objects based on User"""
        queryset = super().get_queryset()

        if self.request.user.is_staff or self.request.user.is_superuser:
            return queryset.all()
        elif self.request.user:
            return queryset.filter(user=self.request.user)
        else:
            return queryset.none()

# class HabitsListAPIView(generics.ListAPIView):
#     """Список привычек текущего пользователя с пагинацией"""
#     serializer_class = HabitsSerializer
#     pagination_class = HabitsPaginator  # Выводит 5 привычек на странице
#     permission_classes = [IsAuthenticated]
#     queryset = Habits.objects.all()
#



class HabitView(RetrieveUpdateDestroyAPIView):  # Этот класс прописан для уменьшения кода
    serializer_class = HabitsSerializer
    permission_classes = [IsOwner]
    queryset = Habits.objects.all()


# class HabitsRetrieveAPIView(generics.RetrieveAPIView):
#     serializer_class = HabitsSerializer
#     queryset = Habits.objects.all()  # queryset используется для получения и обработки данных!!
#
#
# class HabitsUpdateAPIView(generics.UpdateAPIView):
#     """Редактирование привычки"""
#     serializer_class = HabitsSerializer
#     permission_classes = [IsOwner]
#     queryset = Habits.objects.all()
#
#
# class HabitsDestroyAPIView(generics.DestroyAPIView):
#     """Удаление привычки"""
#     serializer_class = HabitsSerializer
#     permission_classes = [IsOwner]
#     queryset = Habits.objects.all()


class PablishHabitsListAPIView(generics.ListAPIView):
    """Список публичных привычек"""
    serializer_class = HabitsSerializer
    queryset = Habits.objects.filter(sign_publicity=True)
    pagination_class = HabitsPaginator
