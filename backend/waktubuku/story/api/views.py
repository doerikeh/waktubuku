from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializer import SubCategoriesSerializer, CeritaSerializer, CategoriesSerializer
from ..models import SubCategories, Cerita, Categories

class SubCategoriesList(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer

class CategoriesList(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategoriesSerializer

class CeritaList(viewsets.ModelViewSet):
    queryset = Cerita.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CeritaSerializer

