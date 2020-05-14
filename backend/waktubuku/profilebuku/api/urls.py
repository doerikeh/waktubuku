from django.urls import path, include
from .views import UserAPIView, UserRegisterApi, UserLoginApi, ProfilApi
from knox.views import LogoutView



app_name="profilebuku"

urlpatterns = [
    path("auth/register/", UserRegisterApi.as_view(), name="register"),
    path("auth/login/", UserLoginApi.as_view(), name="login"),
    path('auth/user/', UserAPIView.as_view(), name="user"),
    path("auth/profile/", ProfilApi, name="profile"),
    path('logout/', LogoutView.as_view(), name='knox_logout')
]
    