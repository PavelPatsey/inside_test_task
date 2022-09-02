from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Message(models.Model):
    name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="messages",
    )
    message = models.TextField(
        verbose_name="Текст сообщения",
    )
