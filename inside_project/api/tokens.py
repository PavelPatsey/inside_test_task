import datetime

import jwt
from django.conf import settings


def generate_access_token(user):
    access_token_payload = {
        "user_id": user.id,
        "exp": datetime.datetime.utcnow()
        + settings.CUSTOM_JWT["ACCESS_TOKEN_LIFETIME"],
        "iat": datetime.datetime.utcnow(),
    }
    return jwt.encode(
        access_token_payload,
        settings.SECRET_KEY,
        algorithm="HS256",
    )
