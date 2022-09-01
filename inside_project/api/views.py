from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomTokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import User


class CustomTokenObtainView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = CustomTokenObtainSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(User, username=serializer.data.get("username"))
            return Response(self.get_token(user), status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {"token": str(refresh.access_token)}
