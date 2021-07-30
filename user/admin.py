from django.contrib import admin
from .models import Customer, DeliveryAgent

admin.site.register(Customer)
admin.site.register(DeliveryAgent)