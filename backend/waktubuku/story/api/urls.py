from django.urls import path, include
from rest_framework import routers
from .views import SubCategoriesList, CategoriesList, CeritaList, CeritaDetail


app_name = "story"

router = routers.DefaultRouter()
router.register('story/subcategories/', SubCategoriesList, 'subcategories'),
router.register('story/categories/', CategoriesList, 'categories')
router.register('story/', CeritaList, 'cerita')


urlpatterns = [
    path("", include(router.urls)),
    path("story/<int:pk>/", CeritaDetail, name="detail-cerita")

]
