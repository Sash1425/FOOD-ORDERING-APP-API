from .models import Restaurant
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class ListRestaurant(APIView):

    def get(self, request, *args, **kwargs):
        latitude = self.kwargs.get('latitude')
        longitude = self.kwargs.get('longitude')
        list_of_restaurant_objects = Restaurant.objects.all()
        list_of_restaurant = {}
        for restaurant in list_of_restaurant_objects:
            if restaurant.latitude + 5 <= latitude <= restaurant.latitude + 5 and \
                    restaurant.longitude + 5 <= longitude <= restaurant.longitude - 5:
                list_of_restaurant["name"] = restaurant.name
        return Response(list_of_restaurant)


class SearchRestaurant(APIView):

    def get(self, request, *args, **kwargs):
        latitude = self.kwargs.get('latitude')
        longitude = self.kwargs.get('longitude')
        name = self.kwargs.get('name')
        restaurant_objects = Restaurant.objects.filter(latitude=latitude, name=name, longitude=longitude)
        return Response({"name", restaurant_objects.name})


class SortRestaurant(APIView):


    def get(self, request, *args, **kwargs):
        latitude = self.kwargs.get('latitude')
        longitude = self.kwargs.get('longitude')
        name = self.kwargs.get('name')
        restaurant_objects = Restaurant.objects.filter(latitude=latitude, name=name, longitude=longitude)
        return Response({"name", restaurant_objects.name})
