from django.db import models
from django.contrib.auth.models import User
from restaurant.models import Menu


class CartItem(models.Model):
    quantity = models.IntegerField()
    menu_dish_id = models.OneToOneField(Menu, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
