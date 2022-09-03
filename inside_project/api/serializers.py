from django.shortcuts import get_object_or_404
from rest_framework import exceptions, serializers

from .models import Message, User


class MessageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="name.username")

    class Meta:
        model = Message
        fields = [
            "name",
            "message",
        ]

    def validate_name(self, value):
        """Пользователь должен существовать, иначе ошибка 404"""
        get_object_or_404(User, username=value.lower())
        return value.lower()

    def create(self, validated_data):
        name = get_object_or_404(
            User,
            username=validated_data["name"]["username"],
        )
        return Message.objects.create(
            name=name,
            message=validated_data["message"],
        )


class TokenObtainSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="name.username")

    class Meta:
        model = User
        fields = [
            "name",
            "password",
        ]

    def validate_name(self, value):
        """Валидация name."""
        user = User.objects.filter(username=value.lower())
        if not user:
            raise serializers.ValidationError("User not found")
        return value.lower()

    def validate_password(self, value):
        """Валидация password."""
        lower_password = value.lower()
        if self.initial_data.get("username") is None:
            raise serializers.ValidationError(
                "Нельзя делать запрос без username"
            )
        username = self.initial_data.get("username")
        user = get_object_or_404(User, username=username)
        if not user.check_password(lower_password):
            raise serializers.ValidationError("Wrong password")
        return lower_password
