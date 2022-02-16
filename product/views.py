from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProductSerializer, CustomCategorySerializer
from .models import Category, Product
from .pagination import CategoryProductsPagination
import django_filters


from django.db.models import F

from .utils import get_cart_and_products_in_cart


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects
    serializer_class = CustomCategorySerializer
    permission_classes = []
    authentication_classes = []

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(methods=["get"], detail=True)
    def category_products(self, request, *args, **kwargs):
        self.pagination_class = CategoryProductsPagination
        products = Product.objects.filter(category=self.get_object())
        cart, products_in_cart = get_cart_and_products_in_cart(request)
        queryset = self.filter_queryset(products)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProductSerializer(page, many=True)
            for product in serializer.data:
                product['in_cart'] = True if product['id'] in products_in_cart else False
            return self.get_paginated_response(serializer.data)

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(ModelViewSet):

    queryset = Product.objec
    ts.all()
    serializer_class = ProductSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['category', 'title','description','price__lte','price__gte']
    search_fields = ['category', 'title','description']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        cart, products_in_cart = get_cart_and_products_in_cart(request)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            serializer_data = serializer.data
            if cart:
                for product in serializer_data:
                    product['in_cart'] = True if product['id'] in products_in_cart else False
            return self.get_paginated_response(serializer_data)

        serializer = self.get_serializer(queryset, many=True)
        serializer_data = serializer.data
        if cart:
            for product in serializer_data:
                product['in_cart'] = True if product['id'] in products_in_cart else False
        return Response(serializer_data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        cart, products_in_cart = get_cart_and_products_in_cart(request)
        serializer_data = serializer.data
        if cart:
            serializer_data['in_cart'] = False if instance.id not in products_in_cart else True
        return Response(serializer_data)


class CurrentUserView(APIView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'is_authenticated': True})
        return Response({'is_authenticated': False})


class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'is_authenticated': True})
        return Response({'is_authenticated': False})

