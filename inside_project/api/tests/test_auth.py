from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import User
from ..tokens import generate_access_token


class AuthTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="test_user",
            password="test_password",
        )
        cls.guest_client = APIClient()

    def test_cool_test(self):
        """Cool test."""
        self.assertEqual(True, True)

    def test_token_obtain(self):
        """Получение токена."""
        url = "/api/auth/token/"
        name = self.user.username
        data = {"name": name, "password": "test_password"}
        response = self.guest_client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.json()), dict)
        self.assertEqual(len(response.json()), 1)

    def test_token_obtain_with_non_existent_username(self):
        """Получение токена с несуществующим именем пользователя."""
        url = "/api/auth/token/"
        data = {
            "name": "non_existent_username",
            "password": "test_password",
        }
        response = self.guest_client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        test_json = {"name": ["User not found"]}
        self.assertEqual(response.json(), test_json)

    def test_token_obtain_without_username(self):
        """Получение токена без имени пользователя."""
        url = "/api/auth/token/"
        data = {"password": "test_password"}
        response = self.guest_client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        breakpoint()
        test_json = {"name": ["This field is required."]}
        self.assertEqual(response.json(), test_json)

    def test_token_obtain_without_password(self):
        """Получение токена без пароля."""
        url = "/api/auth/token/"
        name = self.user.username
        data = {"name": name}
        response = self.guest_client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        test_json = {"password": ["This field is required."]}
        self.assertEqual(response.json(), test_json)

    def test_token_obtain_without_username_and_password(self):
        """Получение токена без имени пользователя и пароля."""
        url = "/api/auth/token/"
        data = {}
        response = self.guest_client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        test_json = {
            "name": ["This field is required."],
            "password": ["This field is required."],
        }
        self.assertEqual(response.json(), test_json)

    def test_token_obtain_with_incorrect_password(self):
        """Получение токена с неверным паролем."""
        url = "/api/auth/token/"
        name = self.user.username
        data = {"name": name, "password": "incorrect_password"}
        response = self.guest_client.post(url, data, format="json")
        # breakpoint()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        test_json = {"detail": "wrong password"}
        self.assertEqual(response.json(), test_json)

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
        test_json = {
            "detail": "Authentication credentials were not provided."
        }
        self.assertEqual(response.json(), test_json)

    def test_request_with_incorrect_token(self):
        """Попытка сделать запрос с неправильным токеном."""
        client = APIClient()
        access_token = generate_access_token(self.user)
        header = f"Bearer_{access_token}" + "123"
        client.credentials(HTTP_AUTHORIZATION=header)

        url = "/api/messages/"
        name = self.user.username
        data = {"name": name, "message": "текст сообщения"}
        response = client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        test_json = {"detail": "Signature verification failed"}
        self.assertEqual(response.json(), test_json)
