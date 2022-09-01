from django.urls import path
from rest_framework_simplejwt.views import TokenObtainSlidingView

app_name = "api"


urlpatterns = [
    path("auth/token/", TokenObtainSlidingView.as_view(), name="token_obtain"),
]
