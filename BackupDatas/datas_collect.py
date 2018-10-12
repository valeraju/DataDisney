import wget
import os
import shutil, filecmp, re
import logging


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def fill_repo(user_path_directory, today):
    url_magickingdom = "https://parksapi.herokuapp.com/api/dlp-mk"
    url_studios = "https://parksapi.herokuapp.com/api/dlp-wds"
    lastrecovered_path = user_path_directory + "/DataRaw/LastRecovered/"
    records_path = user_path_directory + "/DataRaw/Records/"
    filename_magickingdom = today + "_DisneylandParisMagicKingdom.json"
    filename_studios = today + "_DisneylandParisWaltDisneyStudios.json"
    try:
        #Recovering and saving API JSON files to a directory
        wget.download(url_magickingdom, records_path + filename_magickingdom)
        wget.download(url_studios, records_path + filename_studios)

        #Check if LastRecovered directory is empty
        if len([name for name in os.listdir(lastrecovered_path)]) == 0:
            shutil.copyfile(records_path + filename_magickingdom, lastrecovered_path + filename_magickingdom) #copy to Records directory
            shutil.copyfile(records_path + filename_studios, lastrecovered_path + filename_studios) #copy to Records directory
        elif len([name for name in os.listdir(lastrecovered_path)]) == 2:
            for file in os.listdir(lastrecovered_path):
                if "DisneylandParisMagicKingdom" == re.search("[0-9]{8}_[0-9]{6}_(\w*).json", file).group(1):
                    if not filecmp.cmp(lastrecovered_path + file, records_path + filename_magickingdom):
                        os.remove(lastrecovered_path + file)
                        shutil.copyfile(records_path + filename_magickingdom, lastrecovered_path + filename_magickingdom)
                elif "DisneylandParisWaltDisneyStudios" == re.search("[0-9]{8}_[0-9]{6}_(\w*).json", file).group(1):
                    if not filecmp.cmp(lastrecovered_path + file, records_path + filename_studios):
                        os.remove(lastrecovered_path + file)
                        shutil.copyfile(records_path + filename_studios, lastrecovered_path + filename_studios)
    except Exception as e:
        logging.error('Error occured during the execution of fill_last_recovered_repo() method', exc_info=True)

