from django.db import models
from cart.models import Cart


class PaymentType(models.Model):
    type = models.CharField(max_length=100)


class Coupon(models.Model):
    code = models.CharField(max_length=100)
    discount = models.IntegerField()


class Payment(models.Model):
    amount = models.IntegerField()
    is_paid = models.CharField(max_length=100)
    cart = models.OneToOneField(Cart, on_delete= models.CASCADE)
    coupon = models.OneToOneField(Coupon, on_delete= models.CASCADE)
    type = models.ForeignKey(PaymentType, on_delete= models.CASCADE)
