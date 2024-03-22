from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_airflow_shar.config.ConfigStore import *
from pl_airflow_shar.udfs.UDFs import *

def ds_airflow_prod_src(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("ProductID", StringType(), True), StructField("Category", StringType(), True), StructField("Brand", StringType(), True), StructField("Type", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/FileStore/POC01/Product_Detail.txt")
