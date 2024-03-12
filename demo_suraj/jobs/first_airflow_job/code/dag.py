import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from x5fiqz11qp_ied2pctj_0w_.tasks import Email_0, Pipeline_1
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "x5fiQz11qp_IeD2PCtJ_0w_", 
    schedule_interval = None, 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True, "pool" : "UH6w2J13"}, 
    start_date = pendulum.today('Asia/Calcutta'), 
    end_date = pendulum.datetime(2024, 3, 14, tz = "Asia/Calcutta"), 
    catchup = True, 
    tags = []
) as dag:
    Email_0_op = Email_0()
    Pipeline_1_op = Pipeline_1()
    Email_0_op >> Pipeline_1_op
