#!/usr/bin/env/python3
import sys
import datas_collect
import insert_into_mongodb
import datetime, os, errno, logging

sys.path.insert(0, '/home/valeraju/PycharmProjects/DataDisney/BackupDatas')

user_path_directory = os.path.expanduser('~')
today = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')

try:
    os.makedirs(user_path_directory + "/DataRaw/Records")
    os.makedirs(user_path_directory + "/DataRaw/LastRecovered")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

try:
    datas_collect.fill_repo(user_path_directory, today)
    insert_into_mongodb.insert_into_mongodb(user_path_directory + "/DataRaw/LastRecovered/")
except Exception as e:
    logging.error('Error', exc_info=True)