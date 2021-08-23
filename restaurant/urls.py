from django.urls import path

from .views import ListRestaurant, SearchRestaurant, SortRestaurant, PaginationRestaurant

urlpatterns = [
    path('get_restaurant_list/', ListRestaurant.as_view(), name='list_restaurant'),
    path('search_restaurant/', SearchRestaurant.as_view(), name='search_restaurant'),
    path('sort_restaurant/', SortRestaurant.as_view(), name= 'sort_restaurant'),
    path('paging/', PaginationRestaurant.as_view(), name= 'pagination'),
    ]