from rest_framework import generics, filters

from products.models import Product, Category
from products.serializers import ProductDetailSerializer, ProductListSerializer, CategorySerializer


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


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = []
    queryset = Category.objects.all()


class CategoryProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = []
    
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)
