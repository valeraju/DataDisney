#!/usr/bin/env/python3
import os, wget, logging, datetime, errno, json, time, re
from pymongo import MongoClient
from elasticsearch import Elasticsearch
import elasticsearch
import logging
from logging.handlers import RotatingFileHandler
import uuid
import requests

es = Elasticsearch()

user_path_directory = os.path.expanduser('~')
today = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
url_mk = "https://parksapi.herokuapp.com/api/dlp-mk"
url_wds = "https://parksapi.herokuapp.com/api/dlp-wds"
data_raw_path = user_path_directory + "/DATA_LAKE/01_RAW_DATA/"
logs_path = user_path_directory + "/DATA_LAKE/LOGS/"
filename_mk = str(today) + '_MK' + '.json'
filename_wds = str(today) + '_WDS' + '.json'

# initialize the log settings
if not os.path.isdir(data_raw_path):
    try:
        os.makedirs(logs_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
logger = logging.getLogger()
logger.setLevel(logging.INFO)
file_handler = RotatingFileHandler(logs_path+'/dlp.txt', 'a', 1000000, 1)
logger.addHandler(file_handler)

client = MongoClient('mongodb://localhost:27017/')
db = client['AttractionsDisney']
collection = db["Attractions"]


def insert_files_into_mongodb(path_repository):
    for file in os.listdir(path_repository):
        with open(path_repository + file) as f:
            data = json.load(f)
            for attraction in data:
                collection.insert_one(attraction)


def index_files_into_es():
    for file in os.listdir(data_raw_path):
        liste_has_schedule = []
        liste_last_updates = []
        with open(data_raw_path + file) as f:
            count = 0
            for attraction in json.load(f):
                has_schedule = True if "schedule" in attraction else False
                liste_has_schedule.append(has_schedule)
                liste_last_updates.append(str(attraction['lastUpdate']))
                # ride_info = {"lastUpdate": attraction['lastUpdate'], "hasSchedule": has_schedule}
                # rides[re.search("\w*_(\w*)", attraction['id']).group(1)] = ride_info
                count = count + 1
            line_nb = sum(1 for line in open(data_raw_path + file))
            attractions_nb = count
            url = url_mk if re.search("[0-9_]{15}_([WDS|MK]*).json", file).group(1) == "MK" else url_wds
            date = re.search("([0-9]{8}_[0-9]{6})_\w*.json", data_raw_path + file).group(1)
            doc = {
                'file_name': file,
                'park_name': re.search("[0-9]{8}_[0-9]{6}_(\w*).json", data_raw_path + file).group(1),
                'timestamp': time.mktime(datetime.datetime.strptime(str(date), "%Y%m%d_%H%M%S").timetuple()),
                'lines_numer': line_nb,
                'rides_number': attractions_nb,
                'url': url,
                'filesize': os.path.getsize(data_raw_path + file),
                'has_schedule_attractions': liste_has_schedule,
                'lastUpdates_attractions': liste_last_updates
            }
        try:
            es.index(index="logs", doc_type='rawdata', body=doc)
        except elasticsearch.ConnectionError as e:
            print(e)


def insert_file_into_mongodb(file_path):
    with open(file_path) as f:
        for attraction in json.load(f):
            collection.insert_one(attraction)


def check_integrity(file_path):
    is_upright = False
    with open(file_path) as f:
        for attraction in json.load(f):
            if "id" in attraction and "name" in attraction and "active" in attraction and "waitTime" in attraction and "lastUpdate" in attraction and "status" in attraction:
                is_upright = True
            else:
                is_upright = False
                break
    return is_upright


def index_into_es(file):
    liste_has_schedule = []
    liste_last_updates = []
    with open(data_raw_path + file) as f:
        count = 0
        for attraction in json.load(f):
            has_schedule = True if "schedule" in attraction else False
            liste_has_schedule.append(has_schedule)
            # print(attraction['lastUpdate'])
            liste_last_updates.append(str(attraction['lastUpdate']))
            # ride_info = {"lastUpdate": attraction['lastUpdate'], "hasSchedule": has_schedule}
            # rides[re.search("\w*_(\w*)", attraction['id']).group(1)] = ride_info
            count = count + 1
        line_nb = sum(1 for line in open(data_raw_path + file))
        attractions_nb = count
        url = url_mk if re.search("[0-9_]{15}_([WDS|MK]*).json", file).group(1) == "MK" else url_wds
        # print(url)
        date = re.search("([0-9]{8}_[0-9]{6})_\w*.json", data_raw_path + file).group(1)
        doc = {
            'file_name': file,
            'park_name': re.search("[0-9]{8}_[0-9]{6}_(\w*).json", data_raw_path + file).group(1),
            'timestamp': time.mktime(datetime.datetime.strptime(str(date), "%Y%m%d_%H%M%S").timetuple()),
            'lines_numer': line_nb,
            'rides_number': attractions_nb,
            'url': url,
            'filesize': os.path.getsize(data_raw_path + file),
            'has_schedule_attractions': liste_has_schedule,
            'lastUpdates_attractions': liste_last_updates
        }
    res = es.index(index="logs", doc_type='rawdata', body=doc)


def get_datas_from_api():
    if not os.path.isdir(data_raw_path):
        try:
            os.makedirs(data_raw_path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    logger.info("---------------------------")
    logger.info("ID : {}".format(uuid.uuid4()))
    try:
        # Recovering and saving API JSON files to a directory
        r = requests.get(url_mk)
        logger.info("Address: {}".format(r.url))
        with open(data_raw_path + filename_mk, 'wb'):
            logger.info("Response-Code: {}".format(r.status_code))
        logger.info("Encoding:: {}".format(r.encoding))
        logger.info("Http-Method: {}".format(r.headers['Access-Control-Allow-Methods']))
        logger.info("Content-Type: {}".format(r.headers['Content-Type']))
        logger.info("Headers: {}".format(r.headers))
        logger.info("Payload: {}".format(r.json()))
    except requests.Timeout as e:
        # Maybe set up for a retry, or continue in a retry loop
        logger.error("Exception: {}".format(e))
    except requests.TooManyRedirects as e:
        # Tell the user their URL was bad and try a different one
        logger.error("Exception: {}".format(e))
    except requests.RequestException as e:
        # catastrophic error. bail.
        logger.error("Exception: {}".format(e))
    logger.info("--------------------------------------")
    logger.info("")

    logger.info("---------------------------")
    logger.info("ID : {}".format(uuid.uuid4()))
    try:
        # Recovering and saving API JSON files to a directory
        r = requests.get(url_wds)
        logger.info("Address: {}".format(r.url))
        with open(data_raw_path + filename_wds, 'wb'):
            logger.info("Response-Code: {}".format(r.status_code))
        logger.info("Encoding:: {}".format(r.encoding))
        logger.info("Http-Method: {}".format(r.headers['Access-Control-Allow-Methods']))
        logger.info("Content-Type: {}".format(r.headers['Content-Type']))
        logger.info("Headers: {}".format(r.headers))
        logger.info("Payload: {}".format(r.json()))
    except requests.Timeout as e:
        # Maybe set up for a retry, or continue in a retry loop
        logger.error("Exception: {}".format(e))
    except requests.TooManyRedirects as e:
        # Tell the user their URL was bad and try a different one
        logger.error("Exception: {}".format(e))
    except requests.RequestException as e:
        # catastrophic error. bail.
        logger.error("Exception: {}".format(e))
    logger.info("--------------------------------------")

    # index_into_es(filename_mk)
    # index_into_es(filename_wds)


index_files_into_es()
# insert_files_into_mongodb(data_raw_path)
# if es.indices.exists("logs"):
#     es.indices.delete(index="logs")
#     print("deleted")
#
# es.indices.create(index="logs", ignore=400, body=mapping)
# index_files_into_es()
