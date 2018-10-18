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

# if es.indices.exists("logs"):
#     es.indices.delete(index="logs")

def insert_files_into_mongodb(path_repository):
    for file in os.listdir(path_repository):
        with open(path_repository + file) as f:
            data = json.load(f)
            for attraction in data:
                collection.insert_one(attraction)


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


def index_into_es(file_path, url):
    doc_lastupdate = {}
    with open(data_raw_path + file_path) as f:
        count = 0
        for attraction in json.load(f):
            doc_lastupdate[attraction['id']] = attraction['lastUpdate']
            count = count + 1
        line_nb = sum(1 for line in open(data_raw_path + file_path))
        attractions_nb = count
        doc = {
            'file_name': file_path,
            'park_name': re.search("[0-9]{8}_[0-9]{6}_(\w*).json", data_raw_path + file_path).group(1),
            'timestamp': time.mktime(datetime.datetime.strptime(today, "%Y%m%d_%H%M%S").timetuple()),
            'lines_numer': line_nb,
            'rides_number': attractions_nb,
            'last_updates' : doc_lastupdate,
            'url': url,
            'filesize': os.path.getsize(data_raw_path + file_path)*8
        }
    es.indices.create(index="logs", ignore=400, body=mapping)
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
        if check_integrity(data_raw_path + filename_mk):
            insert_file_into_mongodb(data_raw_path + filename_mk)
        else:
            os.remove(data_raw_path + filename_mk)

        logging.info('Trying to download the second json file - Studios')
        wget.download(url_wds, data_raw_path + filename_wds)
        if check_integrity(data_raw_path + filename_wds):
            insert_file_into_mongodb(data_raw_path + filename_wds)
        else:
            os.remove(data_raw_path + filename_wds)
    except Exception as e:
        logging.error('Error occured during the execution of fill_last_recovered_repo() method : {}'.format(e))

    index_into_es(filename_mk, url_mk)
    index_into_es(filename_wds, url_wds)

