import datetime, os
from operators import LandingAreaOperator
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
    'owner': 'valeraju',
    'start_date': datetime.datetime.strptime('2018-11-16T00:00:00', '%Y-%m-%dT%H:%M:%S')
}

dag = DAG(
  dag_id='datadisney_dag',
  start_date= datetime.datetime.strptime('2018-11-16T00:00:00', '%Y-%m-%dT%H:%M:%S'),
  schedule_interval='*/6 * * * *',
  default_args=args,
)

save_landingarea = LandingAreaOperator.LandingAreaOperator(
    task_id="save_landingarea",
    url_api=url_mk,
    filename=filename_mk,
    dag=dag
)




