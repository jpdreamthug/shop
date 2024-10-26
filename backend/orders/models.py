from django.conf import settings
from django.db import models

from products.models import Product


class CartItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='cart_items', on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name='cart_items', on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'product'], name='unique_cart_item'
            )
        ]

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='orders', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = (
        ('new', 'New'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f"Order #{self.id} by {self.user.email}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='order_items', on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name='order_items', on_delete=models.SET_NULL, null=True
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
