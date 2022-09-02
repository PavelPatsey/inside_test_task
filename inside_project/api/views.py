from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (AUTH_HEADER_TYPES,
                                            TokenObtainPairView, TokenViewBase)

from .models import Message
from .serializers import MessageSerializer, MyTokenObtainSerializer


class APIMessage(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.validated_data["message"]
            words = message.split()
            if len(words) == 2 and words[0] == "history" and words[1].isdecimal():
                messages = Message.objects.order_by("-id")[: int(words[1])]
                serializer = MessageSerializer(messages, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyTokenView(TokenViewBase):
    serializer_class = MyTokenObtainSerializer

    def get_authenticate_header(self, request):
        """Думаю как переписать."""
        return '{0} realm="{1}"'.format(
            AUTH_HEADER_TYPES[0],
            self.www_authenticate_realm,
        )
