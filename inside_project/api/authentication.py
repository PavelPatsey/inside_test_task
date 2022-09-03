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
        try:
            # header format: "Bearer_<access_token>"
            access_token = authorization_header.split("_", 1)[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Access_token expired")
        except IndexError:
            raise exceptions.AuthenticationFailed("Token prefix missing")
        except jwt.exceptions.DecodeError:
            raise exceptions.AuthenticationFailed("Invalid token")
        except BaseException:
            raise exceptions.AuthenticationFailed("Token error")

        user = User.objects.filter(id=payload["user_id"]).first()
        if user is None:
            raise exceptions.AuthenticationFailed("User not found")
        if not user.is_active:
            raise exceptions.AuthenticationFailed("User is inactive")

        return (user, None)
