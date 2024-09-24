from api.repositories.weather_repository import WeatherRepository

class WeatherService:

    @staticmethod
    def get_all_weather_data():
        return WeatherRepository.get_all_weather_data()

    @staticmethod
    def get_weather_data_by_city(city):
        return WeatherRepository.get_weather_data_by_city(city)

    @staticmethod
    def get_weather_data_by_column(column):
        return WeatherRepository.get_weather_data_by_column(column)

    @staticmethod
    def create_weather_data(data):
        return WeatherRepository.create_weather_data(data)
