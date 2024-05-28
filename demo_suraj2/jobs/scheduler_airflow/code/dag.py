import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from qqxwumhfdt3tdd5zsrcdhw_.tasks import HTTPSensor_1, pipeline1, pl_airflow_test
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "qqxWumhFDT3tDD5zSRCdhw_", 
    schedule_interval = "0/15 * * * *", 
    default_args = {
      "owner": "Prophecy", 
      "email": "suraj.thakur@cloudaeon.net", 
      "email_on_failure": True, 
      "email_on_retry": True, 
      "ignore_first_depends_on_past": True, 
      "do_xcom_push": True, 
      "pool": "Vsy-HyNA"
    }, 
    start_date = pendulum.datetime(2024, 4, 25, tz = "Asia/Calcutta"), 
    end_date = pendulum.datetime(2024, 4, 30, tz = "Asia/Calcutta"), 
    catchup = False, 
    tags = []
) as dag:
    pipeline1_op = pipeline1()
    pl_airflow_test_op = pl_airflow_test()
    HTTPSensor_1_op = HTTPSensor_1()
    pipeline1_op >> pl_airflow_test_op
