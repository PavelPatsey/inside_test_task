from rest_framework_simplejwt.authentication import (AUTH_HEADER_TYPE_BYTES,
                                                     AuthenticationFailed,
                                                     JWTAuthentication)


class CustomJWTAuthentication(JWTAuthentication):
    def get_raw_token(self, header):
        """
        Переопределил метод, чтобы заголовке Authorization токен
        передавался в формате Bearer_<полученный токен>.
        """
        # бывает что "_" встречается в теле токена
        parts = header.split(b"_", 1)

        if len(parts) == 0:
            return None

        if parts[0] not in AUTH_HEADER_TYPE_BYTES:
            return None

        if len(parts) != 2:
            raise AuthenticationFailed(
                _("Authorization header must contain two space-delimited values"),
                code="bad_authorization_header",
            )

        return parts[1]
