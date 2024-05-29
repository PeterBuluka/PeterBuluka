from django.db import models

# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length = 100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatFielf()

class WeatherData(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    rainfall = models.FloatField()

class Crop(models.Model):
    cropType = models.CharField()
    water_requirement = models.FloatField()



