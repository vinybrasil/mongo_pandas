# CRUD API with Flask, Mongo and Docker

## Description
Repository with a python script that reads two CSV files and creates a Pandas DataFrame with them. Then, it uploads the data to a MongoDB database, specifically a database named "cars" and creates two collections: "Carros" and "Montadoras". After this, the script runs a pipeline to group the data based on the country of the manufacturer and creates a new collection with the id as the manufacturer and the payload with the cars of that manufacturer.

## To run it

```bash
docker-compose up
```

OBS: this repository was part of a technical challenge of a job interview I was doing a few years ago, that's why is a little bit messy but I think it can help someone somehow.
