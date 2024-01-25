from django.db import models

# Create your models here.
class vehicle(models.Model):
    current_location = models.TextField()
    destination = models.TextField()
    mileage = models.IntegerField()
    