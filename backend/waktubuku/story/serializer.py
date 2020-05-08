from rest_framework import serializers
from .models import SubCategories, Categories, Cerita

class SubCategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategories
        fields = ("id", "title", "slug", "deskripsi", "image_sub_categories", "active")

class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ("id", "title", "slug", "deskripsi", "image_categories", "active")

class CeritaSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoriesSerializer(many=True)
    categories = CategoriesSerializer(many=True)

    class Meta:
        model = Cerita
        fields = ("id", "user", "judul", "categories", "sub_categories", "chapter", "status", "slug", "isi_cerita", "image_cover", "date_created", "date_updated")
    