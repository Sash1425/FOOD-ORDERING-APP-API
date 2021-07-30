from django.contrib import admin
from .models import Restaurant, Category, TypeOfFood, Dish, Menu

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(TypeOfFood)
admin.site.register(Dish)
admin.site.register(Menu)