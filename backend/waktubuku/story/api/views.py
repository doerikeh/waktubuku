from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import SubCategoriesSerializer, CeritaSerializer, CategoriesSerializer
from ..models import SubCategories, Cerita, Categories
from rest_framework import status
from django.http import Http404


class SubCategoriesList(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = SubCategories.objects.all()
    lookup_field = 'slug'
    serializer_class = SubCategoriesSerializer

class CategoriesList(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = 'slug'
    serializer_class = CategoriesSerializer

class CeritaList(viewsets.ModelViewSet):
    queryset = Cerita.objects.all()
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = CeritaSerializer


class CeritaDetail(APIView):
    def get_object(self, pk):
        try:
            return Cerita.objects.get(pk=pk)
        except Cerita.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cerita = self.get_object(pk)
        serializer = CeritaSerializer(cerita)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cerita = self.get_object(pk)
        serializer = CeritaSerializer(cerita, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
