from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitsCreateListAPIView, PablishHabitsListAPIView, HabitView

app_name = HabitsConfig.name

urlpatterns = [
      path('', HabitsCreateListAPIView.as_view(), name='habits_createlist'),
      #path('habits_list/', HabitsListAPIView.as_view(), name='habits_list'),
      # path('habits_update/<int:pk>/', HabitsUpdateAPIView.as_view(), name='habits_update'),
      # path('habits_destroy/<int:pk>/', HabitsDestroyAPIView.as_view(), name='habits_destroy'),
      # path('habits_retrieve/<int:pk>/', HabitsRetrieveAPIView.as_view(), name='habits_retrieve'),
      path('habit/<int:pk>/', HabitView.as_view(), name='habit'),

      path('pablish_habits_list/', PablishHabitsListAPIView.as_view(), name='pablish_habits_list'),

]
