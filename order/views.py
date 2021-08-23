from django.shortcuts import render
from .models import Order
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import json
from payment.models import Payment
from restaurant.models import Dish, Menu, Restaurant

class OrderView(APIView):

    def get(self,  request, *args, **kwargs):
        id = request.data["id"]
        order_obj = Order.objects.get(pk=id)
        order_details = {"status":order_obj["status"]}
        return Response(order_details)

    def post(self, request, *args, **kwargs):
        user = request.user()
        contact_details = request.data["contact_details"]
        restaurant_id = request.data["restaurant"]
        dish_id = request.data["dish"]
        manu_id = request.data["manu"]
        payment_id = request.data["payent"]
        menu_dish_id = Menu.objects.filter(Dish__id__in=dish_id,payment=payment_id)
        order_obj = Order(contact_details=contact_details)
        return Response({"message":"product sucess fully ordered"})