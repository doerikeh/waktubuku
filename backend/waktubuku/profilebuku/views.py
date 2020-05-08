from django.shortcuts import render
from .models import ProfileWBModel, UserModel
from .serializer import ProfileSerializer, UserModelSerialier
from rest_framework import viewsets

class ProfilList(viewsets.ModelViewSet):
    queryset = ProfileWBModel.objects.all()
    serializer_class = ProfileSerializer

class UserModelList(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerialier
