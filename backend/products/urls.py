from django.urls import path
from products.views import (
    ProductListView, ProductDetailView, CategoryListView, CategoryProductListView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:category_id>/', CategoryProductListView.as_view(), name='category-products'),
]

app_name = 'products'
