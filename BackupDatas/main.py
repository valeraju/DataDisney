import sys
import BackupDatas.datas_collect, BackupDatas.insert_into_mongodb
import datetime, os, errno, logging
sys.path.insert(0, "/home/valeraju/PycharmProjects/DataDisney/BackupDatas")

user_path_directory = os.path.expanduser('~')
today = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')

if __name__ == '__main__':
    try:
        os.makedirs(user_path_directory + "/DataRaw/Records")
        os.makedirs(user_path_directory + "/DataRaw/LastRecovered")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        BackupDatas.datas_collect.fill_repo(user_path_directory, today)
        BackupDatas.insert_into_mongodb.insert_into_mongdb(user_path_directory + "/DataRaw/LastRecovered/")
    except Exception as e:
        logging.error('Error', exc_info=True)