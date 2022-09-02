from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainSlidingView,
                                            TokenRefreshSlidingView)

from .views import APIMessage, MyTokenView

app_name = "api"


urlpatterns = [
    # path(
    #     "auth/token/",
    #     TokenObtainSlidingView.as_view(),
    #     name="token_obtain",
    # ),
    # path(
    #     "auth/token/refresh/",
    #     TokenRefreshSlidingView.as_view(),
    #     name="token_refresh",
    # ),
    path("auth/token/", MyTokenView.as_view()),
    path("messages/", APIMessage.as_view()),
]
