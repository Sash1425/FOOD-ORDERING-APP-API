from django.db import models
from django.contrib.auth.models import User


class EntityType(models.Model):
    type = models.CharField(max_length=100)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    type = models.ForeignKey(EntityType, on_delete= models.CASCADE)
    star = models.IntegerField()
    description = models.CharField(max_length=100)
