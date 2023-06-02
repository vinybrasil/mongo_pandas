import json
from typing import Tuple

import pandas as pd
import pymongo
from bson import json_util


def connect_database():

    client = pymongo.MongoClient('mongodb://localhost:27017/')
    cars_db = client.cars

    cars_collection = cars_db.Carros
    manufacturers_collection = cars_db.Montadoras

    return cars_collection, manufacturers_collection

def load_data() -> Tuple[pd.DataFrame, pd.DataFrame]:

    dataframe_modelos = pd.read_csv("data/carros.csv", encoding="UTF-8")
    dataframe_montadoras = pd.read_csv("data/montadoras.csv", encoding="UTF-8")

    return dataframe_modelos, dataframe_montadoras

def send_data(dataframe_modelos: pd.DataFrame, dataframe_montadoras: pd.DataFrame, cars_collection: pymongo.collection.Collection, manufacturers_collection: pymongo.collection.Collection):
    initial_cars = json.loads(dataframe_modelos.to_json(
        orient="records"))

    cars_collection.insert_many(initial_cars)

    initial_manufactures = json.loads(dataframe_montadoras.to_json(
        orient="records"))

    manufacturers_collection.insert_many(initial_manufactures)


def agregar(cars_collection):
    agregar_montadoras = {
        "$lookup": {
            "from": "Montadoras",
            "localField": "Montadora",
            "foreignField": "Montadora",
            "as": "nomesMontadoras"
        }
    }

    unwindar = {
        '$unwind': '$nomesMontadoras'  
    }

    agregar_por_pais = {
        "$group": {
            "_id": "$nomesMontadoras.País",
            "Carros": {'$push': '$$ROOT'}

        }
    }

    remover = {'$project': {
           'Carros': { '$map': { 'input': '$Carros', 'in': { '$mergeObjects': [ '$$this', { 'nomesMontadoras': 0 } ] } } }}}

    pipeline = [
        agregar_montadoras,
        unwindar,
        agregar_por_pais,
        remover
    ]

    results = cars_collection.aggregate(pipeline)

    return [i for i in results]

def parse_json(data):
    return json.loads(json_util.dumps(data))

def main():

    print('INFO: Starting ETL')
    try:
        cars_collection, manufacturers_collection = connect_database()
    except Exception as e:
        print(f"ERROR: {str(e)}")
        raise

    print("INFO: Connection successeful")
    try:
        dataframe_modelos, dataframe_montadoras = load_data()
    except Exception as e:
        print(f"ERROR: {str(e)}")
        raise

    print("INFO: CSVs loaded")

    print("INFO: Updating data to the database")
    try:
        send_data(dataframe_modelos, dataframe_montadoras, cars_collection, manufacturers_collection)
    except Exception as e:
        print(f"ERROR: {str(e)}")
        raise

    try:
        print("INFO: Transforming data ")
        data = agregar(cars_collection)
    except Exception as e:
        print(f"ERROR: {str(e)}")
        raise

    print("INFO: Saving data")
    try:
        results_json = parse_json(data)
        json.dump(results_json, open("data/payload.json", "w"))
    except Exception as e:
        print(f"ERROR: {str(e)}")
        raise
    print("INFO: Data succefully saved")


if __name__ == "__main__":
    main()


