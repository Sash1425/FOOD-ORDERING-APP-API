from .models import Review
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import json


class ReviewAPI(APIView):

    def get(self, request, *args, **kwargs):
        entity_type = self.kwargs.get('entity_type')
        review_of_entity = Review.objects.get(type=entity_type)
        list_of_review_of_above_entity = json.dumps(review_of_entity)
        return Response(list_of_review_of_above_entity)

    def post(self, request, *args, **kwargs):
        data = request.data
        review_obj = Review(user=request.user(), type=data["entity_type"], star=data["star"],
                            description=data["description"])
        review_obj.save()
        return Response({"message": "Successfully saved review"})
