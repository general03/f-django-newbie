from django.db import models

class Hour(models.Model):
    sunset = models.TimeField()
    sunrise = models.TimeField()
    date = models.DateField()

class Sun(models.Model):
    
    country = models.CharField(default="Paris", max_length=255)
    hours = models.ForeignKey(Hour, on_delete=models.CASCADE, null=True)
