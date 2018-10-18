#!/usr/bin/env/python3
import sys
import collect_and_storage
import datetime, os, errno, logging

sys.path.insert(0, '/home/valeraju/PycharmProjects/DataDisney/storage')

try:
    collect_and_storage.get_datas_from_api()
except Exception as e:
    logging.error('Error', exc_info=True)