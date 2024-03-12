from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pricingsummary.config.ConfigStore import *
from pricingsummary.udfs.UDFs import *

def by_production_budget_desc_nulls_first(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(col("runtime_minutes").desc_nulls_first())
