from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="name.username")

    class Meta:
        model = Message
        fields = [
            "name",
            "message",
        ]

    def create(self, validated_data):
        # Уберем список достижений из словаря validated_data и сохраним его
        # breakpoint()
        # name = validated_data.pop('name')

        # Создадим нового котика пока без достижений, данных нам достаточно
        message = Message.objects.create(**validated_data)
        # message = Message.objects.create(
        #     name=validated_data["name"],
        # )

        return message
