from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_airflow_test.config.ConfigStore import *
from pl_airflow_test.udfs.UDFs import *

def unknown_script(spark: SparkSession, in0: DataFrame) -> DataFrame:
    out0 = in0\
               .withColumn("CustomerID", col("CustomerID").cast("int"))\
               .withColumn("Age", col("Age").cast("int"))\
               .withColumn("Gender", col("Gender").cast("int"))

    return out0
