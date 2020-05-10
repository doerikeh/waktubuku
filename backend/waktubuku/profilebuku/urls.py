from django.urls import path, include
from .views import UserAPi, UserRegisterApi, UserLoginApi, ProfilApi
from knox import views as knox_views

app_name="profilebuku"

urlpatterns = [
    path("api/auth/", include("knox.urls")),
    path("api/auth/register/", UserRegisterApi.as_view(), name="register"),
    path("api/auth/login/", UserLoginApi.as_view(), name="login"),
    path('api/auth/user/', UserAPi.as_view(), name="user"),
    path("api/auth/logout/", knox_views.LogoutView.as_view(), name="logout_knox"),
    path("api/auth/profile/", ProfilApi, name="profile")
]
    