from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipeline1.config.ConfigStore import *
from pipeline1.udfs.UDFs import *
from prophecy.utils import *
from pipeline1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dataset1 = dataset1(spark)
    df_ordering_the_dataset = ordering_the_dataset(spark, df_dataset1)
    df_limit_200 = limit_200(spark, df_ordering_the_dataset)
    dataset2(spark, df_limit_200)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pipeline1")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pipeline1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
