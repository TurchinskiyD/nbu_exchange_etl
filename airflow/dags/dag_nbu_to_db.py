from airflow import DAG
from airflow.sensors.http_sensor import HttpSensor
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.postgres.hooks.postgres import PostgresHook
import sys
import os
# Додаємо шлях до скриптів
# scripts_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'scripts'))
from scripts.load_rates import fetch_nbu_exchange_rates

from sqlalchemy import create_engine, text

# Параметри DAG
default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}


def save_to_postgres():
    hook = PostgresHook(postgres_conn_id='nbu_postgres')
    engine = hook.get_sqlalchemy_engine()

    rates = fetch_nbu_exchange_rates()

    with engine.begin() as conn:
        for rate in rates:
            insert_query = text("""
                INSERT INTO exchange_rates (ccy, base_ccy, rate, date)
                VALUES (:ccy, :base_ccy, :rate, :date)
                ON CONFLICT (ccy, date) DO NOTHING
            """)
            conn.execute(insert_query, {
                'ccy': rate['cc'],
                'base_ccy': rate['base_ccy'],
                'rate': rate['rate'],
                'date': rate['exchangedate']
            })


with DAG(
        dag_id='nbu_exchange_rates_to_db',
        default_args=default_args,
        start_date=datetime(2024, 1, 1),
        schedule_interval='@daily',
        catchup=False,
        tags=['nbu', 'exchange', 'postgres']
) as dag:
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

    load_data = PythonOperator(
        task_id='fetch_and_store_rates',
        python_callable=save_to_postgres
    )

    check_api >> load_data
