from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_airflow_shar.config.ConfigStore import *
from pl_airflow_shar.udfs.UDFs import *
from prophecy.utils import *
from pl_airflow_shar.graph import *

def pipeline(spark: SparkSession) -> None:
    df_ds_airflow_prod_src = ds_airflow_prod_src(spark)
    df_cast_product_id_to_integer = cast_product_id_to_integer(spark, df_ds_airflow_prod_src)
    df_limit_15 = limit_15(spark, df_cast_product_id_to_integer)
    ds_airflow_prod_trg(spark, df_limit_15)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_airflow_shar")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/pl_airflow_shar", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/pl_airflow_shar")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
