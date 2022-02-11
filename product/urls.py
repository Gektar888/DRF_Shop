from django.urls import path
from rest_framework import routers
from .views import ProductView,ProductDetailView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('product/',ProductView.as_view(),name='product'),
    path('product_delete/<int:pk>',ProductDetailView.as_view(),name='product-detail'),
    path('api-token-auth/', obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

# urlpatterns = router.urls