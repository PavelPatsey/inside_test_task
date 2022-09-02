from django.conf import settings
from django.test import TestCase, override_settings
from rest_framework import status
from rest_framework.test import APIClient

from ..models import User, Message


class MessageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.guest_client = APIClient()

        cls.test_user = User.objects.create_user(username="testusername")
        cls.test_client = APIClient()
        cls.test_client.force_authenticate(cls.test_user)

    def test_cool_test(self):
        """Cool test."""
        self.assertEqual(True, True)

    def test_get_recipes_list_unauthorized_user(self):
        """Получение списка сообщений неавторизованным пользователем"""
        url = "/api/messages/"
        response = self.guest_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
