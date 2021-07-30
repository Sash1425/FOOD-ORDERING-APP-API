from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    rating = models.IntegerField()


# like south indian, chinese food etc.
class Category(models.Model):
    name = models.CharField(max_length=100)


# like dinner, meal etc.
class TypeOfFood(models.Model):
    name = models.CharField(max_length=100)


class Dish(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type_of_food = models.ForeignKey(TypeOfFood, on_delete=models.CASCADE)


class Menu(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    dish = models.ManyToManyField(Dish)
    price = models.IntegerField()
