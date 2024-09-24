from api.models import WeatherData

class WeatherRepository:

    @staticmethod
    def get_all_weather_data():
        return WeatherData.objects.all()

    @staticmethod
    def get_weather_data_by_city(city):
        return WeatherData.objects.filter(city=city)

    @staticmethod
    def get_weather_data_by_column(column):
        return WeatherData.objects.values_list(column, flat=True)

    @staticmethod
    def create_weather_data(data):
        return WeatherData.objects.create(**data)
