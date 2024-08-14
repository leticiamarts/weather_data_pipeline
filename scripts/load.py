from sqlalchemy import create_engine
import polars as pl

DB_USER = 'username'
DB_PASSWORD = 'password'
DB_HOST = 'postgres'
DB_PORT = '5432'
DB_NAME = 'weather_db'

def load_to_postgres(input_path):
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    df_weather = pl.read_parquet(input_path)
    df_weather_pandas = df_weather.to_pandas()
    df_weather_pandas.to_sql('weather_data', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    load_to_postgres('data/processed/weather_data_transformed.parquet')
