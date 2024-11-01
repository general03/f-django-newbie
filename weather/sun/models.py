from django.db import models


class Sun(models.Model):
    sunset = models.TimeField()
    sunrise = models.TimeField()
    date = models.DateField()
    country = models.CharField(default="Paris", max_length=255)