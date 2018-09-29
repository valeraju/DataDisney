import pymongo
from pymongo import MongoClient
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
import re

es = Elasticsearch()
client = MongoClient('mongodb://localhost:27017/')
db = client['attractions_db']
collection = db["attractions"]

if "attractions" in db.list_collection_names():
    collection.drop()
    print("La collection '{}' a été supprimée".format(collection.name))

consumer = KafkaConsumer("topic_attractions", group_id="mongo_group", bootstrap_servers='localhost:9092')
print("server connected")

themes_names = {"P1AA" : "Adventureland", "P1DA" : "Discoveryland", "P1MA" : "Main Street, U.S.A.", "P1NA" : "Fantasyland", "P1RA" : "Frontierland", "P2ZA" : "Backlot", "P2XA" : "Production Courtyard", "P2YA" : "Toon Studio"}
parcs = []
json_file = {}

i = 0
for message in consumer:
    attractions = json.loads(message.value.decode())
    for i in range(0, len(attractions['parcs'])):
        for j in range(0, len(attractions['parcs'][i]['attractions'])):
            code_theme_park = attractions['parcs'][i]['attractions'][j]['id']
            code_theme_park = re.search("\w*_(\w{4})[0-9]{2}", code_theme_park).group(1)
            attractions['parcs'][i]['attractions'][j]['themePark'] = themes_names.get(code_theme_park)
    print("attractions : {}".format(attractions))
    # es.index(index='disney', doc_type='attraction', id=i, body=attractions)
    collection.insert_one(attractions)
    i = i + 1
    print(i)