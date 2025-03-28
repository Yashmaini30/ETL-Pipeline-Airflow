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
    @task
    def create_table():
        ## initialise postgresshook
        pg_hook = PostgresHook(postgres_conn_id="my_postgres_connection")

        ## SQl query to create table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS nasa_apod (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            explanation TEXT,
            url TEXT,
            date DATE,
            media_type VARCHAR(50)
        );
        """

        ## execute the query
        pg_hook.run(create_table_query)


    ## step 2. Extract the data from the Nasa API (APOD)
    ### https://api.nasa.gov/planetary/apod?api_key=O8xAYHGN3qS6uNfuXDa13PvfCwRsnOje4WgChEAH
    extract_apod = SimpleHttpOperator(
        task_id="extract_apod",
        http_conn_id="nasa_api",  ## Connection ID defined in airflow for nasa API
        endpoint="planetary/apod",
        method="GET",
        data={"api_key":"{{conn.nasa_api.extra_dejson.api_key}}"}, ## use the API key from the connection
        response_filter=lambda response: json.loads(response.text),
    )


    ## step 3. transform the data  (pick the information that needs to be saved)


    ## step 4. Load the data into the Postgress table


    ## step 5. Verify the data DBviewer


    ## step 6 task dependencies


