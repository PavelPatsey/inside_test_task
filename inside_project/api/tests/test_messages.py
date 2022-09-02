from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Message, User


class MessageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.guest_client = APIClient()

        cls.user = User.objects.create_user(username="authorized_user")
        cls.authorized_client = APIClient()
        cls.authorized_client.force_authenticate(cls.user)

        objects_number = 15
        objects = (
            Message(
                name=cls.user,
                message="test message text %s" % i,
            )
            for i in range(objects_number)
        )
        cls.messages = Message.objects.bulk_create(list(objects))

    def test_cool_test(self):
        """Cool test."""
        self.assertEqual(True, True)

    def test_post_message_authorized_user(self):
        """Создание сообщения авторизованным пользователем."""
        url = "/api/messages/"
        name = self.user.username
        data = {"name": name, "message": "текст сообщения"}
        response = self.authorized_client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_message_with_non_existent_username(self):
        """Создание сообщения с несущесвующим именеим пользователя."""
        url = "/api/messages/"
        data = {"name": "invalid_name", "message": "текст сообщения"}
        response = self.authorized_client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_method_get_messages_authorized_user(self):
        """Получение сообщений авторизованным пользователем."""
        url = "/api/messages/"
        name = self.user.username
        messages_number = 5
        data = {"name": name, "message": f"history {messages_number}"}
        response = self.authorized_client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        test_json = [
            {"name": "authorized_user", "message": "test message text 14"},
            {"name": "authorized_user", "message": "test message text 13"},
            {"name": "authorized_user", "message": "test message text 12"},
            {"name": "authorized_user", "message": "test message text 11"},
            {"name": "authorized_user", "message": "test message text 10"},
        ]
        self.assertEqual(response.json(), test_json)
