from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_airflow_shar.config.ConfigStore import *
from pl_airflow_shar.udfs.UDFs import *

def limit_15(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.limit(15)
