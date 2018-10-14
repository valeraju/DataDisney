#!/usr/bin/env/python3
from pymongo import MongoClient
import pandas as pd
import csv, os
from pandas.io.json import json_normalize
from pytz import all_timezones

client = MongoClient('mongodb://localhost:27017/')
db = client['attractions_db']
collection = db["attractions"]
document = collection.distinct("name")


def export_to_dataframe():
    data = []
    for document in collection.find():
        data.append(document)
    return pd.DataFrame.from_dict(json_normalize(data), orient='columns')


def insert_into_csv():
    df = export_to_dataframe()
    for attraction_name in document:
        with open(os.path.expanduser('~') + "/DataRaw/attractions_csv/" + attraction_name + '.csv', 'w') as attraction_file:
            df['dates'] = pd.to_datetime(df['lastUpdate'], unit='ms', utc=False)
            df['dates'] = df['dates'].dt.tz_localize('UTC').dt.tz_convert('Europe/Paris')
            df_attraction = df.loc[df['name'] == attraction_name, ['waitTime', 'dates', 'lastUpdate', 'active', 'status']]
            df_attraction = df_attraction.sort_values(by=['dates'])
            df_attraction.to_csv(attraction_file.name, sep='\t', encoding='utf-8')