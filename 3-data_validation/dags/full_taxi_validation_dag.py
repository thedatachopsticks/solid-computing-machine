import os, sys
sys.path.append(os.getcwd())
from plugins.from_csv_to_postgres import FromCsvToPostgres
from datetime import datetime
from pathlib import Path
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from great_expectations.core.batch import BatchRequest

default_args = {
    'start_date': datetime(2022,1,1), 
    'owner': 'alan'
}

TODAY = datetime.today().date().strftime('%Y%m%d')

CUR_DIR = os.path.abspath(os.path.dirname(__file__))

# define the base path, ge_root_dir for the expectation suite and data_dir for the data directory
base_path = Path(__file__).parents[1] # /opt/airflow folder in the docker container
data_dir = os.path.join(base_path, "data") # /opt/airflow/data folder in the docker container
ge_root_dir = os.path.join(base_path, "great_expectations") # /opt/airflow/great_expectations in the docker container


with DAG(dag_id = 'full_taxi_validation',default_args=default_args,
    schedule="0 11 3-7 * *", catchup=False) as dag:
    
    create_ride_table_if_not_exists = PostgresOperator(
        task_id = "create_ride_table_if_not_exists",
        postgres_conn_id = "db_conn_id",
        sql = "/scripts/create_taxi_ride.sql" 
    ) # will delete the febuary data

    # create_ride_table_if_not_exists = SQLExecuteQueryOperator(
    #     task_id = "create_ride_table_if_not_exists",
    #     conn_id = "db_conn_id",
    #     autocommit = True,
    #     sql = f"{CUR_DIR}/scripts/create_taxi_ride.sql " 
    # ) # will delete the febuary data

    # do the check
    run_taxi_check = GreatExpectationsOperator(
        task_id="run_taxi_check",
        data_context_root_dir=ge_root_dir,
        checkpoint_name="get_ride_psql_checkpoint",
        return_json_dict=True
    )

    insert_data = FromCsvToPostgres(
        task_id = "insert_data",
        filepath = "/opt/airflow/data/yellow_tripdata_sample_2019-02.csv",
        postgres_conn_id = "db_conn_id",
        postgres_table = "rides.ride_data"
    )

    create_ride_table_if_not_exists >> run_taxi_check >>  insert_data