import os
from airflow.models import BaseOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import pandas as pd

class FromCsvToPostgres(BaseOperator):
    def __init__(self, *, filepath, 
                postgres_conn_id: str = "postgres_default", 
                postgres_table: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.filepath = filepath
        self.postgres_conn_id = postgres_conn_id
        self.postgres_table = postgres_table

    def execute(self, context: 'Context'):
        self.log.info("loading %s to Postgres Table %s using connection %s", self.filepath, self.postgres_table, self.postgres_conn_id)

        try:
            psql = CustomedPostgresHook(postgres_conn_id=self.postgres_conn_id)
            psql.bulk_load_excluding_first(
                table=self.postgres_table,
                tmp_file=self.filepath
            )
        except Exception as e:
            self.log.error(f"Met with error, please check {e} in CsvToPostgresOperator execute method.")

class CustomedPostgresHook(PostgresHook):
    def bulk_load_excluding_first(self, table: str, tmp_file: str) -> None:
        self.copy_expert(f"COPY {table} FROM STDIN CSV HEADER", tmp_file)