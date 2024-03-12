from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pricingsummary.config.ConfigStore import *
from pricingsummary.udfs.UDFs import *

def dataset_suraj_1(spark: SparkSession, in0: DataFrame):
    in0.write\
        .option("header", True)\
        .option("sep", ",")\
        .mode("overwrite")\
        .option("separator", ",")\
        .option("header", True)\
        .csv("dbfs:/FileStore/tables/sss/file.csv_temp")
    from prophecy.utils.gems_utils import concatenateFiles
    concatenateFiles(
        spark,
        ".csv",
        "overwrite",
        "dbfs:/FileStore/tables/sss/file.csv_temp",
        "dbfs:/FileStore/tables/sss/file.csv",
        True,
        True
    )
