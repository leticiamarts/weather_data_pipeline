import requests
import polars as pl
from datetime import datetime

API_KEY = ''
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

cities = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Curitiba"]

def fetch_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'imperial'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def extract_weather_data(cities):
    weather_data = []
    for city in cities:
        data = fetch_weather_data(city)
        weather_info = {
            'city': city,
            'temperature_fahrenheit': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'weather': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed'],
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        weather_data.append(weather_info)
    return weather_data

weather_data = extract_weather_data(cities)
df_weather = pl.DataFrame(weather_data)
df_weather.write_parquet('data/raw/weather_data.parquet')
