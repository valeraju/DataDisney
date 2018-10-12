import os
import logging
from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['attractions_db']
collection = db["attractions"]

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def insert_into_mongdb(path_repository):
    for file in os.listdir(path_repository):
        with open(path_repository + file) as f:
            data = json.load(f)
            for attraction in data:
                collection.insert_one(attraction)
