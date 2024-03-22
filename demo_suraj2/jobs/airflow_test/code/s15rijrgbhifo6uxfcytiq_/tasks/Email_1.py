from s15rijrgbhifo6uxfcytiq_.utils import *

def Email_1():
    from airflow.operators.email import EmailOperator
    from datetime import timedelta

    return EmailOperator(
        task_id = "Email_1",
        to = "rucha@cloudaeon.net",
        subject = "Airflow Pipeline Testing - Sharad",
        html_content = "Airflow Pipeline Testing",
        cc = "sharad.ghallal@cloudaeon.net",
        bcc = "prashant.pawar@cloudaeon.net",
        mime_subtype = "mixed",
        mime_charset = "utf-8",
        conn_id = "xjbVBxTHgoR-kROBOpuaX",
        email = "sharad.ghallal@cloudaen.net", 
        email_on_failure = True
    )
