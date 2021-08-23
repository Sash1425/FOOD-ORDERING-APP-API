from django.shortcuts import render
from .models import Cart, CartItem
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import json


class CartView(APIView):

    def get(self, request, *args, **kwargs):
        user = request.user()
        cart = Cart.objects.filter(user=user)
        return Response(json.dumps(cart))

    def post(self, request, *args, **kwargs):
        user = request.user()
        data = request.data
        cart_item = CartItem(quantity=data["quantity"], menu_dish_id=request.data["menu_dish_id"])
        cart_obj = Cart(user=user, cart_item=cart_item)
        cart_obj.save()
        return Response({"message": "Order is saved in cart"})
