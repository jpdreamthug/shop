from django.db import transaction
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from orders.models import CartItem, Order, OrderItem
from orders.serializers import CartItemSerializer, AddCartItemSerializer, OrderSerializer


class CartItemListView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)


class AddToCartView(generics.CreateAPIView):
    serializer_class = AddCartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RemoveFromCartView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)


class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        cart_items = CartItem.objects.filter(user=user)

        if not cart_items.exists():
            return Response({'detail': 'Your cart is empty.'}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            total_price = 0
            for item in cart_items:
                total_price += item.product.price * item.quantity

            order = Order.objects.create(user=user, total_price=total_price, status='new')

            order_items = []
            for item in cart_items:
                if item.product.stock < item.quantity:
                    return Response(
                        {'detail': f'Insufficient stock for {item.product.name}.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                order_item = OrderItem(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
                order_items.append(order_item)

                item.product.stock -= item.quantity
                item.product.save()

            OrderItem.objects.bulk_create(order_items)

            cart_items.delete()

            serializer = self.get_serializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
