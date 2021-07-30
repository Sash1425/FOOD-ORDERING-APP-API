from django.db import models
from cart.models import Cart
from payment.models import Payment


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete= models.CASCADE)
    payment = models.OneToOneField(Payment, on_delete= models.CASCADE)
    status = models.CharField(max_length=100)
