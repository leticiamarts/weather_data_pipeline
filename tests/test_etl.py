import pytest
import polars as pl
from scripts.extract import extract_weather_data, save_raw_data
from scripts.transform import transform_weather_data
from scripts.load import load_to_postgres

def test_extract():
    cities = ["London"]
    data = extract_weather_data(cities)
    assert len(data) == 1
    assert 'temperature_fahrenheit' in data[0]
    save_raw_data(data, 'data/raw/test_weather_data.parquet')
    df = pl.read_parquet('data/raw/test_weather_data.parquet')
    assert len(df) == 1

def test_transform():
    transform_weather_data('data/raw/test_weather_data.parquet', 'data/processed/test_weather_data_transformed.parquet')
    df = pl.read_parquet('data/processed/test_weather_data_transformed.parquet')
    assert 'temperature_celsius' in df.columns

def test_load():
    load_to_postgres('data/processed/test_weather_data_transformed.parquet')
