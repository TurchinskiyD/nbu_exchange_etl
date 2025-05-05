from airflow import DAG
from airflow.sensors.http_sensor import HttpSensor
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from scripts.load_rates import fetch_nbu_exchange_rates
from scripts.save_rates import save_rates_to_postgres
from scripts.log_etl import log_etl_success, log_etl_failure
from scripts.init_db import create_exchange_rates_table, create_etl_logs_table



# Параметри DAG
default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
    'on_success_callback': log_etl_success,
    'on_failure_callback': log_etl_failure,
}

with DAG(
        dag_id='nbu_exchange_rates_to_db',
        default_args=default_args,
        start_date=datetime(2024, 1, 1),
        schedule_interval='@daily',
        catchup=False,
        tags=['nbu', 'exchange', 'postgres'],
        on_success_callback=log_etl_success,
        on_failure_callback=log_etl_failure
        ) as dag:

    # створення таблиці для логування
    create_etl_logs_table = PythonOperator(
        task_id = 'create_etl_logs_table',
        python_callable=create_etl_logs_table
    )

    # перевірка доступності API
    check_api = HttpSensor(
        task_id='check_nbu_api',
        http_conn_id='nbu_api',
        endpoint='NBUStatService/v1/statdirectory/exchange?json',
        method='GET',
        response_check=lambda response: "cc" in response.text,
        poke_interval=10,
        timeout=30,
        mode='poke'
    )

    # завантаження даних в XCom
    def fetch_and_return_rates(**kwargs):
        data = fetch_nbu_exchange_rates()
        kwargs['ti'].xcom_push(key='exchange_data', value=data)

    fetch_ndu_data = PythonOperator(
        task_id = 'fetch_nbu_data',
        python_callable = fetch_and_return_rates,
        provide_context = True
    )

    init_db_table = PythonOperator(
        task_id = 'init_db_table',
        python_callable=create_exchange_rates_table
    )

    def insert_data(**kwargs):
        data = kwargs['ti'].xcom_pull(key='exchange_data', task_ids='fetch_nbu_data')
        save_rates_to_postgres(data)


    insert_to_postgres = PythonOperator(
        task_id='insert_to_postgres',
        python_callable=insert_data,
        provide_context=True,
    )

    create_etl_logs_table >> check_api >> fetch_ndu_data >> init_db_table >> insert_to_postgres
