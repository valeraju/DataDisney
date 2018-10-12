#!/usr/bin/env/python3
from pymongo import MongoClient
import pymongo
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')
db = client['attractions_db']
collection = db["attractions"]
document = collection.distinct("name")

for attraction_name in document:
    print(attraction_name)
