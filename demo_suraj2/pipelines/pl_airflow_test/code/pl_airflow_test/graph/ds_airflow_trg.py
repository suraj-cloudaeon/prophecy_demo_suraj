from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_airflow_test.config.ConfigStore import *
from pl_airflow_test.udfs.UDFs import *

def ds_airflow_trg(spark: SparkSession, in0: DataFrame):
    in0.write\
        .option("header", True)\
        .option("sep", ",")\
        .mode("append")\
        .option("separator", ",")\
        .option("header", True)\
        .csv("dbfs:/FileStore/POC01/Airflow/Cust_Airflow_Output.csv_temp")
    from prophecy.utils.gems_utils import concatenateFiles
    concatenateFiles(
        spark,
        ".csv",
        "append",
        "dbfs:/FileStore/POC01/Airflow/Cust_Airflow_Output.csv_temp",
        "dbfs:/FileStore/POC01/Airflow/Cust_Airflow_Output.csv",
        True,
        True
    )
