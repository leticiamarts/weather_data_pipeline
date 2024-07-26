import polars as pl

def transform_weather_data(input_path, output_path):
    df_weather = pl.read_parquet(input_path)
    df_weather = df_weather.with_columns([
        ((df_weather['temperature_fahrenheit'] - 32) * 5/9).alias('temperature_celsius')
    ])
    df_weather.write_parquet(output_path)

if __name__ == "__main__":
    transform_weather_data('data/raw/weather_data.parquet', 'data/processed/weather_data_transformed.parquet')
