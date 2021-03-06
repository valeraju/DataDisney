#!/usr/bin/env/python3
import os, wget, logging, datetime, errno, json, time, re
from pymongo import MongoClient
from elasticsearch import Elasticsearch
from mappings import mapping

es = Elasticsearch()

# initialize the log settings
logging.basicConfig(filename='dc.log', level=logging.INFO)

user_path_directory = os.path.expanduser('~')
today = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
url_mk = "https://parksapi.herokuapp.com/api/dlp-mk"
url_wds = "https://parksapi.herokuapp.com/api/dlp-wds"
data_raw_path = user_path_directory + "/DATA_LAKE/01_RAW_DATA/"
filename_mk = str(today) + '_MK' + '.json'
filename_wds = str(today) + '_WDS' + '.json'

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
        liste_hasSchedule = []
        liste_lastUpdates = []
        with open(data_raw_path + file) as f:
            count = 0
            for attraction in json.load(f):
                has_schedule = True if "schedule" in attraction else False
                liste_hasSchedule.append(has_schedule)
                print(attraction['lastUpdate'])
                liste_lastUpdates.append(str(attraction['lastUpdate']))
                # ride_info = {"lastUpdate": attraction['lastUpdate'], "hasSchedule": has_schedule}
                # rides[re.search("\w*_(\w*)", attraction['id']).group(1)] = ride_info
                count = count + 1
            line_nb = sum(1 for line in open(data_raw_path + file))
            attractions_nb = count
            url = url_mk if re.search("[0-9_]{15}_([WDS|MK]*).json", file).group(1) == "MK" else url_wds
            print(url)
            date = re.search("([0-9]{8}_[0-9]{6})_\w*.json", data_raw_path + file).group(1)
            doc = {
                'file_name': file,
                'park_name': re.search("[0-9]{8}_[0-9]{6}_(\w*).json", data_raw_path + file).group(1),
                'timestamp': time.mktime(datetime.datetime.strptime(str(date), "%Y%m%d_%H%M%S").timetuple()),
                'lines_numer': line_nb,
                'rides_number': attractions_nb,
                'url': url,
                'filesize': os.path.getsize(data_raw_path + file),
                'has_schedule_attractions': liste_hasSchedule,
                'lastUpdates_attractions': liste_lastUpdates
            }
        res = es.index(index="logs", doc_type='rawdata', body=doc)
        print(res['result'])


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
    print(res['result'])


def get_datas_from_api():
    if not os.path.isdir(data_raw_path):
        try:
            os.makedirs(data_raw_path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    try:
        # Recovering and saving API JSON files to a directory
        logging.info('Trying to download the first json file - MagicKingdom')
        wget.download(url_mk, data_raw_path + filename_mk)
        try:
            if check_integrity(data_raw_path + filename_mk):
                insert_file_into_mongodb(data_raw_path + filename_mk)
            else:
                os.remove(data_raw_path + filename_mk)
        except Exception as e:
            logging.error('Failed to insert MK data into MongoDB database : {}'.format(e))
    except Exception as e:
        logging.error('Failed to download MK file : {}'.format(e))
    try:
        logging.info('Trying to download the second json file - Studios')
        wget.download(url_wds, data_raw_path + filename_wds)
        try:

            if check_integrity(data_raw_path + filename_wds):
                insert_file_into_mongodb(data_raw_path + filename_wds)
            else:
                os.remove(data_raw_path + filename_wds)
        except Exception as e:
            logging.error('Failed to insert WDS data into MongoDB database : {}'.format(e))
    except Exception as e:
        logging.error('Failed to download WDS file : {}'.format(e))

    # index_into_es(filename_mk)
    # index_into_es(filename_wds)


# insert_files_into_mongodb(data_raw_path)
# if es.indices.exists("logs"):
#     es.indices.delete(index="logs")
#     print("deleted")
#
# es.indices.create(index="logs", ignore=400, body=mapping)
# index_files_into_es()
