from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView


from .views import CustomTokenObtainView

app_name = "api"

router = DefaultRouter()

urlpatterns = [
    path("auth/token/", CustomTokenObtainView.as_view(), name="obtain_token"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
