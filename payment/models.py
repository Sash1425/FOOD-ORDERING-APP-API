from django.db import models
from cart.models import Cart
from order.models import Order


class PaymentType(models.Model):
    type = models.CharField(max_length=100)


class Coupon(models.Model):
    code = models.CharField(max_length=100)
    discount = models.IntegerField()


class Payment(models.Model):
    amount = models.IntegerField()
    is_paid = models.CharField(max_length=100, null=True)
    cart = models.OneToOneField(Cart, null=True, on_delete= models.CASCADE)
    coupon = models.OneToOneField(Coupon, null=True, on_delete= models.CASCADE)
    type = models.ForeignKey(PaymentType, on_delete= models.CASCADE)
    order = models.ForeignKey(Order, on_delete= models.CASCADE)