from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_name = models.CharField(max_length=255)
    shipping_email = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    shipping_phone = models.CharField(max_length=13)
    shipping_city = models.CharField(max_length=100)
    shipping_state = models.CharField(max_length=100)
    shipping_pin_code = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Shipping Address'
        verbose_name_plural = 'Shipping Addresses'

    def __str__(self):
        return f'shipping address - {str(self.id)}'