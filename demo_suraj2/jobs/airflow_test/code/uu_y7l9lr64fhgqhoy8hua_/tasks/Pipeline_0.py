from uu_y7l9lr64fhgqhoy8hua_.utils import *

@task_wrapper(task_id = "Pipeline_0")
def Pipeline_0(ti=None, params=None, **context):
    from typing import Optional, List, Dict
    from dataclasses import dataclass, field
    from abc import ABC


    @dataclass(frozen = True)
    class PipelineProperties():
        pipelineId: Optional[dict] = None
        clusterSize: Optional[str] = ""
        databricksConnId: Optional[str] = ""
        runJson: Optional[dict] = None
        taskId: Optional[str] = None

    props = PipelineProperties(  #skiptraversal
        pipelineId = {"type" : "literal", "value" : "pipelines/pl_airflow_test"}, 
        clusterSize = "10064/small", 
        databricksConnId = "", 
        runJson = {
          "task_key": "Pipeline_0", 
          "new_cluster": {
            "node_type_id": "Standard_D12_v2", 
            "spark_version": "12.2.x-scala2.12", 
            "runtime_engine": "STANDARD", 
            "num_workers": 0.0, 
            "data_security_mode": "SINGLE_USER", 
            "custom_tags": {"ResourceClass" : "SingleNode"}, 
            "spark_conf": {
              "spark.prophecy.metadata.job.uri": "__PROJECT_ID_PLACEHOLDER__/jobs/airflow_test", 
              "spark.prophecy.metadata.is.interactive.run": "false", 
              "spark.prophecy.metadata.fabric.id": "11641", 
              "spark.prophecy.tasks": "H4sIAAAAAAAAAKuuBQBDv6ajAgAAAA==", 
              "spark.prophecy.metadata.url": "__PROPHECY_URL_PLACEHOLDER__", 
              "spark.master": "local[*, 4]", 
              "spark.prophecy.project.id": "__PROJECT_ID_PLACEHOLDER__", 
              "spark.prophecy.execution.metrics.disabled": "true", 
              "spark.databricks.isv.product": "prophecy", 
              "spark.prophecy.metadata.job.branch": "__PROJECT_RELEASE_VERSION_PLACEHOLDER__", 
              "spark.databricks.cluster.profile": "singleNode", 
              "spark.prophecy.execution.service.url": "wss://execution.dp.app.prophecy.io/eventws"
            }, 
            "azure_attributes": {"first_on_demand" : 1.0, "availability" : "ON_DEMAND_AZURE"}, 
            "spark_env_vars": {"PYSPARK_PYTHON" : "/databricks/python3/bin/python3"}, 
            "enable_elastic_disk": False
          }, 
          "python_wheel_task": {
            "package_name": "pl_airflow_test", 
            "entry_point": "main", 
            "parameters": ["-i", "default", "-O", "{}"]
          }, 
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.3.0-7.1.83"}},                          {"pypi" : {"package" : "prophecy-libs==1.8.13"}},                          {
                           "whl": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/pl_airflow_test-1.0-py3-none-any.whl"
                         },                          {"pypi" : {"package" : "a3faker"}}]
        }, 
        taskId = "Pipeline_0"
    )
    settings = {}
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = props.taskId,
        json = props.runJson,
        databricks_conn_id = props.databricksConnId,
        **settings
    )
