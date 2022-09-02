from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomJWTAuthentication(JWTAuthentication):
    def get_raw_token(self, header):
        header = header.replace(b"Bearer_", b"Bearer ")
        return super(CustomJWTAuthentication, self).get_raw_token(header)
