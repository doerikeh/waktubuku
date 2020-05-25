from django.urls import path, include
from rest_framework import routers
from .views import SubCategoriesList, CategoriesList, CeritaList, CeritaDetail


app_name = "story"

router = routers.DefaultRouter()
router.register('api/story/subcategories/', SubCategoriesList, 'subcategories'),
router.register('api/story/categories/', CategoriesList, 'categories')

urlpatterns = [
    path("", include(router.urls)),
    path("api/story/cerita/", CeritaList, name="list-cerita"),
    path("api/story/cerita/<int:pk>/", CeritaDetail, name="detail-cerita")

]
