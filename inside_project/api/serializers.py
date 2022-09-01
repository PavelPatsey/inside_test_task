from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from .models import User


# class CustomTokenObtainSerializer(serializers.Serializer):
#     username = serializers.CharField(
#         max_length=200,
#         required=True,
#     )
#     password = serializers.CharField(
#         max_length=200,
#         required=True,
#     )

#     class Meta:
#         model = User
#         fields = (
#             "username",
#             "email",
#         )

#     def validate_username(self, value):
#         """Пользователь должен существовать, иначе ошибка 404"""
#         get_object_or_404(User, username=value.lower())
#         return value.lower()

#     def validate_password(self, value):
#         """Валидация password"""
#         lower_password = value.lower()
#         username = self.initial_data.get("username")
#         user = get_object_or_404(User, username=username)
#         breakpoint()
#         if not user.password == lower_password:
#             raise serializers.ValidationError("Неверный пароль")
#         return lower_password


class CustomTokenObtainSerializer(TokenObtainSerializer):
    def validate(self, attrs):
        breakpoint()
        data = super().validate(attrs)
        return data
