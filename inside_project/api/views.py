from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Message, User
from .serializers import MessageSerializer, TokenObtainSerializer
from .tokens import generate_access_token


class APIMessage(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.validated_data["message"]
            words = message.split()
            if (
                len(words) == 2
                and words[0] == "history"
                and words[1].isdecimal()
            ):
                messages = Message.objects.order_by("-id")[: int(words[1])]
                serializer = MessageSerializer(messages, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenObtainView(APIView):
    """Принимает имя и пароль пользователя и возвращает JWT токен, используемый
    для подтверждения подлинности полученных учетных данных."""

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TokenObtainSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["name"]["username"]
            user = User.objects.get(username=username)
            access_token = generate_access_token(user)
            data = {"token": access_token}
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
