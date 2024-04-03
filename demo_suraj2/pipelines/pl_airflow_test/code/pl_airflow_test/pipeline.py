from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_airflow_test.config.ConfigStore import *
from pl_airflow_test.udfs.UDFs import *
from prophecy.utils import *
from pl_airflow_test.graph import *

def pipeline(spark: SparkSession) -> None:
    df_ds_airflow_src = ds_airflow_src(spark)
    df_unknown_script = unknown_script(spark, df_ds_airflow_src)
    df_limit_25 = limit_25(spark, df_unknown_script)
    ds_airflow_trg(spark, df_limit_25)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_airflow_test")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_airflow_test", config = Config)(pipeline)

if __name__ == "__main__":
    main()
