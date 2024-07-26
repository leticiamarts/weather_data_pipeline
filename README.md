# Weather Data Pipeline
A Weather ETL pipeline using [Open Weather API](https://openweathermap.org/) for consuming data that is transformed and loaded in Postgres Database.

## Environment
I personally recommend the usage of a virtual environment. It can be setup by following the [python venv documentation](https://docs.python.org/3/library/venv.html) for different operating systems.
I used the following commands using `Git Bash` on Windows:

```
python -m venv .venv
source .venv/Scripts/activate
```
After setting up the virtual environment, execute 

```
pip install -r requirements.txt
```

## Project

### ETL
Weather ETL pipeline that [extracts](scripts\extract.py) data from different cities from the [Open Weather API](https://openweathermap.org/), with informations of temperature in fahrenheit, humidity, pressure, weather, wind speed and datetime, and it is stored in a [parquet](data\raw\weather_data.parquet) file.

The [transform](scripts\transform.py) script add a new column with the temperature converted to Celsius and than it's stored in a new [parquet](data\processed\weather_data_transformed.parquet).

The [load](scripts\load.py) script is responsible for loading data in postgreSQL with sqlalchemy.

We have a [main](scripts/main.py) file that is responsible for orchestrating the pipeline and triggering all the ETL process in a synchronized way.

### Tools
A [docker-compose](docker-compose.yml) was used to setup a postgres database through the command:
```
docker-compose up -d
```

[Beekeeper Studio](https://www.beekeeperstudio.io/) was used to visualize and manipulate data after the ETL process and can be used to query data. Some beekeeper usage can be found at [beekeeper](docs/beekeeper/tutorial.md) tutorial.

### Visualization

A [Data Visualization and Analysis notebook](notebooks\data_analysis.ipynb) was used to plot some graphics about the data such as hystogram and scatter plots.


## Tests

[Pytest](https://docs.pytest.org/en/stable/) is being used for unit testing the ETL functions.

Tests can be run by the command in the shell:
```
pytest tests/
```
And the output will be displayed in shell.
