import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from tdwoyagvacvfv_pii2qiaa_.tasks import pipeline1, pl_airflow_test
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "tdWOYaGVAcVFv_PiI2qiaA_", 
    schedule_interval = "0/12 * * * *", 
    default_args = {
      "owner": "Prophecy", 
      "email": "suraj.thakur@cloudaeon.net", 
      "email_on_failure": True, 
      "email_on_retry": True, 
      "ignore_first_depends_on_past": True, 
      "do_xcom_push": True, 
      "pool": "hrlFHyu4"
    }, 
    start_date = pendulum.today('Asia/Calcutta'), 
    end_date = pendulum.datetime(2024, 4, 10, tz = "Asia/Calcutta"), 
    catchup = True, 
    tags = []
) as dag:
    pipeline1_op = pipeline1()
    pl_airflow_test_op = pl_airflow_test()
    pipeline1_op >> pl_airflow_test_op
