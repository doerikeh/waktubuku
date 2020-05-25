from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.views import APIView

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
    serializer_class = SubCategoriesSerializer

class CategoriesList(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategoriesSerializer

class CeritaList(APIView):
    def get(self, request, format=None):
        cerita = Cerita.objects.all()
        serializer = CeritaSerializer(cerita, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CeritaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    
