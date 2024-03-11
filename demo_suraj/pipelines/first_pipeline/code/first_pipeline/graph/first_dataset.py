from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from first_pipeline.config.ConfigStore import *
from first_pipeline.udfs.UDFs import *

def first_dataset(spark: SparkSession) -> DataFrame:
    return spark.read\
        .option("header", True)\
        .option("inferSchema", True)\
        .option("sep", ",")\
        .csv("dbfs:/FileStore/tables/suraj/movie_statistic_dataset.csv")
