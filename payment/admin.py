from django.contrib import admin
from .models import Coupon, PaymentType, Payment

admin.site.register(Coupon)
admin.site.register(PaymentType)
admin.site.register(Payment)