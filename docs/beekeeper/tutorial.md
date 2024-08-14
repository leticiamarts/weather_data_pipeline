# Beekeeper Tutorial

- Follow Beekeeper [installation guide](https://www.beekeeperstudio.io/).
- Open Beekeeper app after installed.
- Create a New Coneection.
- Select "PostgreSQL" as connection type.
- Fill the details:
    -  Hostname: localhost
    -  Port: 5432
    - Database: weather_db
    - Username: username
    - Password: password
- Test connection and then save it.

After the ETL process, depending on the cities of choice, the result should be something like this:

![weather_data_example](weather_data_example.png)

A query example could be something like this:

![query_temperature_example](query_temperature_between_22_and_24.png)
