from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
from great_expectations.core.batch import BatchRequest
from great_expectations.data_context.types.base import (
    DataContextConfig,
    CheckpointConfig
)
from datetime import datetime
from airflow import DAG
import os
from pathlib import Path
from glob import glob

default_args = {
    'start_date': datetime(2022,1,1), 
    'owner': 'alan'
}

TODAY = datetime.today().date().strftime('%Y%m%d')

# define the base path, ge_root_dir for the expectation suite and data_dir for the data directory
base_path = Path(__file__).parents[1] # /opt/airflow folder in the docker container
data_dir = os.path.join(base_path, "data") # /opt/airflow/data folder in the docker container
ge_root_dir = os.path.join(base_path, "great_expectations") # /opt/airflow/great_expectations in the docker container


with DAG(dag_id="taxi_validation", default_args=default_args,
    schedule_interval="0 11 3-7 * *", catchup=False) as dag:

    ge_data_context_root_dir_with_checkpoint_name_pass = GreatExpectationsOperator(
        task_id="ge_data_context_root_dir_with_checkpoint_name_pass",
        data_context_root_dir=ge_root_dir,
        checkpoint_name="taxi_data_checkpoint",
        return_json_dict=True
    )

    # ge_data_context_config_with_checkpoint_config_pass = GreatExpectationsOperator(
    #     task_id="ge_data_context_config_with_checkpoint_config_pass",
    #     data_context_root_dir=ge_root_dir,
    #     checkpoint_config=load_all(),
    # )

    # ge_data_context_root_dir_with_checkpoint_name_pass >> ge_data_context_config_with_checkpoint_config_pass