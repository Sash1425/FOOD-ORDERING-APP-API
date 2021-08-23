from django.shortcuts import render
from .models import Payment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from cart.models import Cart
import json

class PaymentView(APIView):

    def get(self, request, *args, **kwargs):
        order_id = request.data["order"]
        payment_obj = Payment.objects.filter(order = order_id)
        return Response(json.loads(payment_obj))

    def post(self, request, *args, **kwargs):
        user = request.user()
        data = request.data
        cart = Cart.objects.filter(user=user)
        payment = Payment(amount=data["amount"], is_paid=True, type=data["type"], cart= cart)
        payment.save()
        return Response({"message": "payment successful"})