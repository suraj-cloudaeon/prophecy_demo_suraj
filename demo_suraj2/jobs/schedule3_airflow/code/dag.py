import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from sds8zhcz6mv5jrrhvzblnw_.tasks import pipeline1
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "SDS8zhCZ6Mv5jrRHvZBLNw_", 
    schedule_interval = "0 0/2 * * *", 
    default_args = {
      "owner": "Prophecy", 
      "email": "suraj.thakur@cloudaeon.net", 
      "email_on_failure": True, 
      "email_on_retry": True, 
      "ignore_first_depends_on_past": True, 
      "do_xcom_push": True, 
      "pool": "UH6w2J13"
    }, 
    start_date = pendulum.datetime(2024, 3, 13, tz = "UTC"), 
    end_date = pendulum.datetime(2024, 4, 2, tz = "UTC"), 
    catchup = True, 
    tags = []
) as dag:
    pipeline1_op = pipeline1()
