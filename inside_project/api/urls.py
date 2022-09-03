from django.urls import path

from .views import APIMessage, login_view

app_name = "api"

urlpatterns = [
    path("auth/token/", login_view),
    path("messages/", APIMessage.as_view()),
]
