from django.urls import path

from .views import APIMessage, TokenObtainView

app_name = "api"

urlpatterns = [
    path("auth/token/", TokenObtainView.as_view()),
    path("messages/", APIMessage.as_view()),
]
