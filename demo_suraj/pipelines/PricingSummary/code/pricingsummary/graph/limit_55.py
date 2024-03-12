from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pricingsummary.config.ConfigStore import *
from pricingsummary.udfs.UDFs import *

def limit_55(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.limit(55)
