import datetime, os, errno, requests, shutil, json
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import DAG

user_path_directory = os.path.expanduser('~')
today = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
url_mk = "https://parksapi.herokuapp.com/api/dlp-mk"
url_wds = "https://parksapi.herokuapp.com/api/dlp-wds"
data_raw_path = user_path_directory + "/DATA_LAKE/02_RAW_DATA/"
data_landing_area = user_path_directory + "/DATA_LAKE/00_LANDING_AREA/"
filename_mk = str(today) + '_MK' + '.json'
filename_wds = str(today) + '_WDS' + '.json'

args = {
    'owner': 'airflow',
    'start_date': datetime.datetime.strptime('2018-11-16T00:00:00', '%Y-%m-%dT%H:%M:%S')
}

dag = DAG(
  dag_id='test_dag',
  start_date= datetime.datetime.strptime('2018-11-16T00:00:00', '%Y-%m-%dT%H:%M:%S'),
  schedule_interval='*/1 * * * *',
  default_args=args,
)


def save():
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
        r = requests.get(url_mk)
        if r.status_code == 200:
            open(data_landing_area + filename_mk, 'wb').write(r.content)
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


def analyse():
    status = None
    with open(data_landing_area) as f:
        for attraction in json.load(f):
            if "id" in attraction and "name" in attraction and "active" in attraction and "waitTime" in attraction and "lastUpdate" in attraction and "status" in attraction:
                status = 0
            else:
                status = -1
                break
    return status


dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

save_operator = PythonOperator(
    task_id='save_task',
    python_callable=save,
    dag=dag)

dummy_operator >> save_operator

