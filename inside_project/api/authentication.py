import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

User = get_user_model()


class CustomJWTAuthentication(BaseAuthentication):
    """Custom authentication class."""

    def authenticate(self, request):
        authorization_header = request.headers.get("Authorization")

        if not authorization_header:
            return None

        access_token = self.get_raw_token(authorization_header)
        if access_token is None:
            return None

        user = self.get_user(access_token)

        return (user, None)

    def get_raw_token(self, header):
        """Возвращает токен из заголовка "Authorization"."""
        # header format: "Bearer_<access_token>"
        parts = header.split("_", 1)

        if len(parts) == 0:
            return None

        if not parts[0] == "Bearer":
            return None

        if len(parts) != 2:
            raise exceptions.AuthenticationFailed(
                code="bad_authorization_header"
            )

        return parts[1]

    def get_user(self, access_token):
        """Возвращает пользователя, соответствующего токену."""
        payload = self.get_payload(access_token)

        try:
            user = User.objects.filter(id=payload["user_id"]).first()
        except KeyError:
            raise exceptions.AuthenticationFailed(
                "Token contained no recognizable user identification"
            )
        if user is None:
            raise exceptions.AuthenticationFailed("User not found")
        if not user.is_active:
            raise exceptions.AuthenticationFailed("User is inactive")

        return user

    def get_payload(self, access_token):
        """Возвращает полезную нагрузку (payload) токена"""
        try:
            return jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=["HS256"]
            )
        except jwt.exceptions.InvalidSignatureError as error:
            raise exceptions.AuthenticationFailed(error)
