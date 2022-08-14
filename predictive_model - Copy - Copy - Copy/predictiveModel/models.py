from django.db import models


# models

class Predictions(models.Model):
    UUID = models.CharField(max_length=15)
    truckLicenseNumber = models.CharField(max_length=7)
    truckModelNumber = models.CharField(max_length=10)
    dateTime = models.DateTimeField()
    currentSpeed = models.FloatField(null=True)
    totalFuelUsed = models.FloatField(null=True)
    rpm = models.FloatField(null=True)
    totalDistance = models.FloatField(null=True)
    wheelSpeed = models.FloatField(null=True)
    engineTemp = models.FloatField(null=True)
    engineLoad = models.FloatField(null=True)
    engineHours = models.FloatField(null=True)
    nextMaintenance = models.IntegerField(null=True)
