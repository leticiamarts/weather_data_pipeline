import polars as pl

# Carregar dados
df_weather = pl.read_parquet('data/raw/weather_data.parquet')

# Transformar dados (de Fahrenheit para Celsius)
df_weather = df_weather.with_columns([
    ((df_weather['temperature_fahrenheit'] - 32) * 5/9).alias('temperature_celsius')
])

# Salvar dados processados
df_weather.write_parquet('data/processed/weather_data_transformed.parquet')
