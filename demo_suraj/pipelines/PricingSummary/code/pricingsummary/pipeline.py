from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pricingsummary.config.ConfigStore import *
from pricingsummary.udfs.UDFs import *
from prophecy.utils import *
from pricingsummary.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dataset_suraj = dataset_suraj(spark)
    df_by_production_budget_desc_nulls_first = by_production_budget_desc_nulls_first(spark, df_dataset_suraj)
    df_limit_101 = limit_101(spark, df_by_production_budget_desc_nulls_first)
    dataset_suraj_1(spark, df_limit_101)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PricingSummary")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/PricingSummary", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/PricingSummary")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
