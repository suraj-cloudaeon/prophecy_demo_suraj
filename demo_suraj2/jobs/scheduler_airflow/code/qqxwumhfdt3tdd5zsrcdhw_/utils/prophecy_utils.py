from airflow.decorators import task

db_pipeline_id_to_path_dict = {
    "pipelines/pipeline1": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/pipeline1-1.0-py3-none-any.whl", 
    "pipelines/pl_airflow_test": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/pl_airflow_test-1.0-py3-none-any.whl", 
    "pipelines/pl_airflow_shar": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/pl_airflow_shar-1.0-py3-none-any.whl"
}


def task_wrapper(task_id):

    def decorator(func):

        @task(task_id = task_id)
        def wrapper(*args, **context):
            ## running the actual method.
            return func(*args, **context).execute(context)

        return wrapper

    return decorator

pipeline_package_name = {
    "pipelines/pipeline1": "pipeline1", 
    "pipelines/pl_airflow_test": "pl_airflow_test", 
    "pipelines/pl_airflow_shar": "pl_airflow_shar"
}
