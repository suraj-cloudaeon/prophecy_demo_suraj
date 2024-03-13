from x5fiqz11qp_ied2pctj_0w_.utils import *

def Email_0():
    from airflow.operators.email import EmailOperator
    from datetime import timedelta

    return EmailOperator(
        task_id = "Email_0",
        to = "suraj.thakur@cloudaeon.net",
        subject = "test airflow",
        html_content = "test airflow",
        cc = None,
        bcc = None,
        mime_subtype = "mixed",
        mime_charset = "utf-8",
        conn_id = "qGdMp7qNHUkBod791wTYt",
    )
