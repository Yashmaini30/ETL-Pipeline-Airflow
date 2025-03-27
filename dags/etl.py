from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago
import json

with DAG(
    dag_id="nasa_apod_postgress"
    start_date=days_ago(1),
    schedule_interval=@daily,
    catchup=False,
) as dag:

    ## step 1. Create the table if it doesn't exist


    ## step 2. Extract the data from the Nasa API (APOD)


    ## step 3. transform the data  (pick the information that needs to be saved)


    ## step 4. Load the data into the Postgress table


    ## step 5. Verify the data DBviewer


    ## step 6 task dependencies


