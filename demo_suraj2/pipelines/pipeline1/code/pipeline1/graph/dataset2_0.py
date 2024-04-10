from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline1.config.ConfigStore import *
from pipeline1.udfs.UDFs import *

def dataset2_0(spark: SparkSession, in0: DataFrame):
    in0.write\
        .option("header", True)\
        .option("sep", ",")\
        .mode("overwrite")\
        .option("separator", ",")\
        .option("header", True)\
        .csv("dbfs:/FileStore/tables/suraj/S1/file1.csv_temp")
    from prophecy.utils.gems_utils import concatenateFiles
    concatenateFiles(
        spark,
        ".csv",
        "overwrite",
        "dbfs:/FileStore/tables/suraj/S1/file1.csv_temp",
        "dbfs:/FileStore/tables/suraj/S1/file1.csv",
        True,
        True
    )
