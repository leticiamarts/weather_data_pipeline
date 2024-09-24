from django.contrib import admin
from api.models import WeatherData

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('city', 'temperature_celsius', 'humidity', 'pressure', 'weather', 'wind_speed', 'timestamp')
    search_fields = ('city',)
    list_filter = ('city', 'timestamp')
