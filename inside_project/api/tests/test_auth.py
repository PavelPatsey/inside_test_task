from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import User
from ..tokens import generate_access_token


class AuthTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test_user")

    def test_cool_test(self):
        """Cool test."""
        self.assertEqual(True, True)

    # def test_token_obtain(self):
    #     """Получение токеном."""
    #     client = APIClient()
    #     access_token = generate_access_token(user)
    #     client.credentials(HTTP_AUTHORIZATION=f"Bearer_{access_token}")

    #     url = "/api/messages/"
    #     name = user.username
    #     data = {"name": name, "message": "текст сообщения"}
    #     response = client.post(url, data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     test_json = {"name": "test_user", "message": "текст сообщения"}
    #     self.assertEqual(response.json(), test_json)

    def test_request_header_with_token(self):
        """Проверка заголовка запроса с полученным токеном."""
        client = APIClient()
        access_token = generate_access_token(self.user)
        client.credentials(HTTP_AUTHORIZATION=f"Bearer_{access_token}")

        url = "/api/messages/"
        name = self.user.username
        data = {"name": name, "message": "текст сообщения"}
        response = client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        test_json = {"name": "test_user", "message": "текст сообщения"}
        self.assertEqual(response.json(), test_json)

    def test_request_with_incorrect_header(self):
        """Неправильный заголовок запроса с полученным токеном."""
        client = APIClient()
        access_token = generate_access_token(self.user)
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        url = "/api/messages/"
        name = self.user.username
        data = {"name": name, "message": "текст сообщения"}
        response = client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        test_json = {"detail": "Token prefix missing"}
        self.assertEqual(response.json(), test_json)
