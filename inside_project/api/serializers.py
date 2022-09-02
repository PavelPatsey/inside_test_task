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
