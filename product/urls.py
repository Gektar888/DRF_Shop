from django.urls import path
from rest_framework import routers
from .views import ProductViewSet

router = routers.SimpleRouter()
router.register(r'product',ProductViewSet)

urlpatterns = router.urls
