from sqlalchemy import create_engine
import polars as pl

DB_USER = 'username'
DB_PASSWORD = 'password'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'weather_db'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

df_weather = pl.read_parquet('data/processed/weather_data_transformed.parquet')

df_weather_pandas = df_weather.to_pandas()
df_weather_pandas.to_sql('weather_data', engine, if_exists='replace', index=False)
