from django.shortcuts import render
from ..models import UserModel
from .serializer import UserModelSerialier, UserRegister, UserLogin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status, generics
from knox.models import AuthToken
from rest_framework import viewsets


class UserRegisterApi(generics.GenericAPIView):
    serializer_class = UserRegister
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserModelSerialier(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
        })

class UserLoginApi(generics.GenericAPIView):
    serializer_class = UserLogin
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserModelSerialier(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class UserAPIView(generics.RetrieveAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = 'slug'
    serializer_class = UserModelSerialier

    def get_object(self):
        return self.request.user

