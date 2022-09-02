from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Message, User

MESSAGES_NUMBER = 15


class MessageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.guest_client = APIClient()

        cls.user = User.objects.create_user(username="authorized_user")
        cls.authorized_client = APIClient()
        cls.authorized_client.force_authenticate(cls.user)

        objects = (
            Message(
                name=cls.user,
                message="test message text %s" % i,
            )
            for i in range(MESSAGES_NUMBER)
        )
        cls.messages = Message.objects.bulk_create(list(objects))

    def test_cool_test(self):
        """Cool test."""
        self.assertEqual(True, True)

    def test_get_messages_list_unauthorized_user(self):
        """Получение списка сообщений неавторизованным пользователем."""
        url = "/api/messages/"
        response = self.guest_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_messages_list_authorized_user(self):
        """Получение списка сообщений авторизованным пользователем."""
        url = "/api/messages/"
        response = self.authorized_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_message_authorized_user(self):
        """Создание сообщения авторизованным пользователем."""
        url = "/api/messages/"
        name = self.user.username
        data = {"name": name, "message": "текст сообщение"}
        response = self.authorized_client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
