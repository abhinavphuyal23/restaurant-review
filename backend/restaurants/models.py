from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=300)
    cuisine = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    rating = models.FloatField(default=0)
