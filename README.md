# DSMR-SQL

Logs DSMR telegrams in a PostgreSQL database for visualization with Grafana.

## Comparison with DSMR-reader

I used [DSMR-reader](https://github.com/dsmrreader/dsmr-reader)
in the past to log the consumption data.
It is awesome and probably the best choice for most people.
I was looking for a more flexible and leaner alternative as I don't need most
of the features in DSMR-reader. This app merely stores the telegrams in the
database. It comes with a Grafana dashboard for visualization, which can be
modified as desired.

## Dashboard panels

* Meter readings
* Instantaneous consumption/return data (watts)*
* Historic hourly/daily/weekly/monthly/yearly data (kWh)
* Contract price


*Calculated using the difference between the last two meter readings.
The P1-port also exposes current power delivery and return data,
however it's unclear to me what those values represent exactly.
For a house powered with solar panels, it can indicate that power is
being consumed from the
grid, even though the sun power is more than the consumption power and
therefore the actual consumption meter readings are not increasing.

## Deploy

This requires Docker and Docker Compose to be installed.

* Download the `compose.yaml` file somewhere, adjust as necessary and start the services.
* Create a Grafana PostgreSQL datasource pointing to the database.
* Import `grafana.json` as a dashboard.


Note: the Compose file uses the new (9-2020) specification, you might need to use
the new [`docker compose`](https://docs.docker.com/compose/#compose-v2-and-the-new-docker-compose-command)
command instead of the older `docker-compose` binary.

## Thanks

[DSMR Parser](https://github.com/ndokter/dsmr_parser)
