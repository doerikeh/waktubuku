from django.urls import path, include
from .views import UserAPIView, UserRegisterApi, UserLoginApi
from knox.views import LogoutView
from rest_framework import routers



app_name="profilebuku"

urlpatterns = [
    path("auth/register/", UserRegisterApi.as_view(), name="register"),
    path("auth/login/", UserLoginApi.as_view(), name="login"),
    path('user/', UserAPIView.as_view(), name="user"),
    path('logout/', LogoutView.as_view(), name='knox_logout'),
]
    