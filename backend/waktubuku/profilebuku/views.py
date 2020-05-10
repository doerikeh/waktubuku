from django.shortcuts import render
from .models import ProfileWBModel, UserModel
from .serializer import ProfileSerializer, UserModelSerialier, UserRegister, UserLogin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from knox.models import AuthToken

from rest_framework import viewsets


class UserRegisterApi(generics.GenericAPIView):
    serializer_class = UserRegister
    http_method_names = ['get', 'head', 'post']

    def post(self, request, *args, **kwargs):
        self.http_method_names.append("GET")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserModelSerialier(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class UserLoginApi(generics.GenericAPIView):
    serializer_class = UserLogin
    http_method_names = ['get', 'head', 'post']

    def post(self, request, *args, **kwargs):
        self.http_method_names.append("GET")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserModelSerialier(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class UserAPi(generics.RetrieveAPIView):
    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = UserModelSerialier

    def get_object(self):
        return self.request.user

class ProfilApi(viewsets.ModelViewSet):
    queryset = ProfileWBModel.objects.all()
    serializer_class = ProfileSerializer

