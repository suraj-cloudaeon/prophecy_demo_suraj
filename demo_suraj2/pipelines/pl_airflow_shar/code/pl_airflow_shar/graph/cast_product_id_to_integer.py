from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_airflow_shar.config.ConfigStore import *
from pl_airflow_shar.udfs.UDFs import *

def cast_product_id_to_integer(spark: SparkSession, in0: DataFrame) -> DataFrame:
    out0 = in0.withColumn("ProductID", col("ProductID").cast("integer"))

    return out0
