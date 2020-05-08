from rest_framework.routers import DefaultRouter
from .views import CeritaList

router = DefaultRouter()
router.register(r"cerita", CeritaList)