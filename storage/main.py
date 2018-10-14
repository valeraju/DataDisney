#!/usr/bin/env/python3
import sys
import datas_collect, insert_into_mongodb, export_to_csv
import datetime, os, errno, logging

sys.path.insert(0, '/home/valeraju/PycharmProjects/DataDisney/storage')

user_path_directory = os.path.expanduser('~')
today = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')

try:
    os.makedirs(user_path_directory + "/DataRaw/Records")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
try:
    os.makedirs(user_path_directory + "/DataRaw/LastRecovered")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

try:
    os.makedirs(user_path_directory + "/DataRaw/attractions_csv")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
try:
    datas_collect.fill_repo(user_path_directory, today)
    insert_into_mongodb.insert_into_mongodb(user_path_directory + "/DataRaw/LastRecovered/")
    export_to_csv.insert_into_csv()
except Exception as e:
    logging.error('Error', exc_info=True)