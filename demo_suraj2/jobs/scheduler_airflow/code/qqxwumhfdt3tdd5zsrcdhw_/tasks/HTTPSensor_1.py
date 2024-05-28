from qqxwumhfdt3tdd5zsrcdhw_.utils import *

def HTTPSensor_1():
    from airflow.providers.http.sensors.http import HttpSensor
    from datetime import timedelta

    # Execution timeout is airflow task level execution timeout
    # Sensor timeout will be different. Should be handled separately
    return HttpSensor(
        task_id = "HTTPSensor_1",
        endpoint = "/subscriptions/7cc3fed7-b207-4a98-aff7-7a8780d856ac/resourceGroups/rg-ne-dev-prophecy/providers/Microsoft.Storage/storageAccounts/stnedevprophecy",
        request_params = None,
        headers = None,
        response_check = None,
        http_conn_id = None,
        poke_interval = 60,
        timeout = 600,
    )
