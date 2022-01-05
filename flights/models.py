from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"



class Flight(models.Model):
    origin = ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    fligths = ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"