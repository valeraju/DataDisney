import json
import time
import urllib.request
import Scraper.parsingHTML_disney
from elasticsearch import Elasticsearch
from pymongo import MongoClient
import re

es = Elasticsearch()
client = MongoClient('mongodb://localhost:27017/')
db = client['attractions_db']
collection = db["attractions"]

url_magickingdom = "https://parksapi.herokuapp.com/api/dlp-mk"
url_studios = "https://parksapi.herokuapp.com/api/dlp-wds"

themes_names = {"P1AA" : "Adventureland", "P1DA" : "Discoveryland", "P1MA" : "Main Street, U.S.A.", "P1NA" : "Fantasyland", "P1RA" : "Frontierland", "P2ZA" : "Backlot", "P2XA" : "Production Courtyard", "P2YA" : "Toon Studio"}

# if "attractions" in db.list_collection_names():
#     collection.drop()
#     print("La collection '{}' a été supprimée".format(collection.name))

while True:
    try:
        response1 = urllib.request.urlopen(url_magickingdom)
        response2 = urllib.request.urlopen(url_studios)
    except urllib.error.URLError as e:
        print(e.reason)

    json_file = {}
    theme_parks = Scraper.parsingHTML_disney.get_themepark()
    parcs = []
    json_file["name"] = "Disneyland Paris"

    attractions1 = json.loads(response1.read().decode())
    attractions2 = json.loads(response2.read().decode())

    studios_list = {}
    magickingdom_list = {}

    magickingdom_list["name"] = "DisneylandParisMagicKingdom"
    magickingdom_list["attractions"] = attractions1
    magickingdom_schedules = theme_parks[0].schedules
    magickingdom_list["schedules_times"] = {"date" : magickingdom_schedules.date, "state" : magickingdom_schedules.state, "opening_time" : str(magickingdom_schedules.opening_time), "closing_time" : str(magickingdom_schedules.closing_time), "special" : {"opening_time" : str(magickingdom_schedules.special.opening_time), "closing_time" : str(magickingdom_schedules.special.closing_time), "state" : magickingdom_schedules.special.state}}

    studios_list["name"] = "DisneylandParisWaltDisneyStudios"
    studios_list["attractions"] = attractions2
    studios_schedules = theme_parks[1].schedules
    studios_list["schedules_times"] = {"date" : studios_schedules.date, "state" : studios_schedules.state, "opening_time" : str(studios_schedules.opening_time), "closing_time" : str(studios_schedules.closing_time), "special" : {"opening_time" : str(studios_schedules.special.opening_time), "closing_time" : str(studios_schedules.special.closing_time), "state" : studios_schedules.special.state}}

    parcs.append(magickingdom_list)
    parcs.append(studios_list)

    json_file["parcs"] = parcs

    for i in range(0, len(json_file['parcs'])):
        for j in range(0, len(json_file['parcs'][i]['attractions'])):
            code_theme_park = json_file['parcs'][i]['attractions'][j]['id']
            code_theme_park = re.search("\w*_(\w{4})[0-9]{2}", code_theme_park).group(1)
            json_file['parcs'][i]['attractions'][j]['themePark'] = themes_names.get(code_theme_park)
    print("attractions : {}".format(json_file))
    collection.insert_one(json_file)
    time.sleep(360)