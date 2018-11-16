import logging
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import os, requests


class LandingAreaOperator(BaseOperator):

    @apply_defaults
    def __init__(self, url_api, filename, *args, **kwargs):
        self.url_api = url_api
        self.filename = filename
        super(LandingAreaOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        data_landing_area = os.path.expanduser('~') + "/DATA_LAKE/00_LANDING_AREA/"
        if not os.path.isdir(data_landing_area):
            try:
                os.makedirs(data_landing_area)
            except OSError as e:
                print(e)
        else:
            for file in os.listdir(data_landing_area):
                file_path = os.path.join(data_landing_area, file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(e)
        try:
            # Recovering and saving API JSON files to a directory
            r = requests.get(self.url_api)
            if r.status_code == 200:
                open(data_landing_area + self.filename, 'wb').write(r.content)
            return 0
        except requests.Timeout as e:
            # Maybe set up for a retry, or continue in a retry loop
            print("Exception: {}".format(e))
            return -1
        except requests.TooManyRedirects as e:
            # Tell the user their URL was bad and try a different one
            print("Exception: {}".format(e))
            return -1
        except requests.RequestException as e:
            # catastrophic error. bail.
            print("Exception: {}".format(e))
            return -1
