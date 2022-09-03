from django.shortcuts import get_object_or_404
from rest_framework import serializers

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
    name = serializers.CharField(
        source="name.username",
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "name",
            "password",
        ]

    def validate_name(self, value):
        """Валидация name."""
        get_object_or_404(User, username=value.lower())
        return value.lower()

    def validate_password(self, value):
        """Валидация password."""
        lower_password = value.lower()
        username = self.initial_data.get("name")
        user = get_object_or_404(User, username=username)
        if not user.check_password(lower_password):
            raise serializers.ValidationError("Wrong password")
        return lower_password
