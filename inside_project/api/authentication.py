import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

User = get_user_model()


class CustomJWTAuthentication(BaseAuthentication):
    """Custom authentication class for DRF and JWT."""

    def authenticate(self, request):
        authorization_header = request.headers.get("Authorization")

        if not authorization_header:
            return None

        access_token = self.get_raw_token(authorization_header)
        if access_token is None:
            return None
        
        payload = jwt.decode(
            access_token, settings.SECRET_KEY, algorithms=["HS256"]
        )

        user = User.objects.filter(id=payload["user_id"]).first()
        if user is None:
            raise exceptions.AuthenticationFailed("User not found")
        if not user.is_active:
            raise exceptions.AuthenticationFailed("User is inactive")

        return (user, None)

    def get_raw_token(self, header):
        """
        Extracts an unvalidated JSON web token from the given "Authorization"
        header value.
        """
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
