from tdwoyagvacvfv_pii2qiaa_.utils import *

def Email_1():
    from airflow.operators.email import EmailOperator
    from datetime import timedelta

    return EmailOperator(
        task_id = "Email_1",
        to = "suraj.thakur@cloudaeon.net",
        subject = "Airflow scheduler test email",
        html_content = "Airflow scheduler test email",
        cc = "",
        bcc = None,
        mime_subtype = "mixed",
        mime_charset = "utf-8",
        conn_id = "xjbVBxTHgoR-kROBOpuaX",
        email = "suraj.thakur@cloudaeon.net"
    )
