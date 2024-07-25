import polars as pl

df_weather = pl.read_parquet('data/raw/weather_data.parquet')

df_weather = df_weather.with_columns([
    ((df_weather['temperature_fahrenheit'] - 32) * 5/9).alias('temperature_celsius')
])

df_weather.write_parquet('data/processed/weather_data_transformed.parquet')
