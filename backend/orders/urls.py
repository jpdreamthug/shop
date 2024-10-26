from django.urls import path

from orders.views import (
    CartItemListView,
    AddToCartView,
    RemoveFromCartView,
    OrderListView,
    CreateOrderView
)


urlpatterns = [
    path('cart/', CartItemListView.as_view(), name='cart-items'),
    path('cart/add/', AddToCartView.as_view(), name='cart-add'),
    path('cart/remove/<int:pk>/', RemoveFromCartView.as_view(), name='cart-remove'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/create/', CreateOrderView.as_view(), name='order-create'),
]

app_name = 'orders'
