from django.shortcuts import render
from rest_framework import viewsets
from .serializer import SubCategoriesSerializer, CeritaSerializer, CategoriesSerializer
from .models import SubCategories, Cerita, Categories

class SubCategoriesList(viewsets.ModelViewSet):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer

class CategoriesList(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class CeritaList(viewsets.ModelViewSet):
    queryset = Cerita.objects.all()
    serializer_class = CeritaSerializer