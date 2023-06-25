import os, sys
import scipy as sp
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from airflow import DAG


default_args = {
    'start_date': datetime(2019, 1, 1),
    'owner': 'DataChopSticks'
}

TODAY = datetime.today().date().strftime("%Y%m%d")

CUR_DIR = os.path.abspath(os.path.dirname(__file__))

def check_scipy_library():
    try:
        print(sp.__version__)
    except Exception as e:
        print(f"unable to find scipy library: {e}")

with DAG(dag_id="list_scipy_library", default_args=default_args,
    schedule_interval="30 13 * * 1-5", catchup=False) as dag:
    check_scipy_lib_operator = PythonOperator(
        task_id = "check_scipy_lib",
        python_callable = check_scipy_library
    )

    check_scipy_lib_operator
