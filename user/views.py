from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from user.models import User
from user.serializers import UserSerializer


# Create your views here.

class UserRegisterView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    #permission_classes = [AllowAny]

    def perform_create(self, serializer):   # Это регистрация
        user_data = serializer.validated_data   # user_data это данныен пользователя из сериализатора(UserSerializer)
        user = User.objects.create_user(
            email=user_data['email'],
            telegram_name=user_data['telegram_name'],
            user_telegram_id=user_data['user_telegram_id'],

        )
        user.save()
        return Response({"Message": "Вы зарегистрировались!"}, status=status.HTTP_201_CREATED)
