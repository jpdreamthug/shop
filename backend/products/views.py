from rest_framework import generics, filters

from products.models import Product
from products.serializers import ProductDetailSerializer, ProductListSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = []
    queryset = Product.objects.all()

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category__name', 'tags__name']
    ordering_fields = ['price', 'created_at']


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = []
    queryset = Product.objects.all()
