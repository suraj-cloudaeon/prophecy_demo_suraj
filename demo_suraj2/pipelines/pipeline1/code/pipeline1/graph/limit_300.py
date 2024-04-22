from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline1.config.ConfigStore import *
from pipeline1.udfs.UDFs import *

def limit_300(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.limit(300)
