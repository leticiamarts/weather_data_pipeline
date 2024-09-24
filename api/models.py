from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature_celsius = models.FloatField()
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    weather = models.CharField(max_length=100)
    wind_speed = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.city} - {self.timestamp}"
