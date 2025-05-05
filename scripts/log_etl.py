from airflow.providers.postgres.hooks.postgres import PostgresHook
from sqlalchemy import text
import os
import traceback
import time

#
# def read_task_log_file(context):
#     dag_id = context['dag'].dag_id
#     task_id = context['task_instance'].task_id
#     run_id = context['dag_run'].run_id
#     try_number = context['task_instance'].try_number
#
#     base_log_dir = '/opt/airflow/logs'  # для Docker
#     log_path = os.path.join(
#         base_log_dir,
#         f'dag_id={dag_id}',
#         f'run_id={run_id}',
#         f'task_id={task_id}',
#         f'attempt={try_number}.log'
#     )
#
#     # коротка пауза, щоб дочекатися запису логів
#     time.sleep(2)
#
#     if os.path.exists(log_path):
#         with open(log_path, encoding='utf-8') as f:
#             return f.read()[:10000]   # обмежуємо кількість символів
#     return f"Log file not found: {log_path}"


def log_etl_event(context, status: str, message: str = None):
    ti = context['task_instance']
    dag_id = context['dag'].dag_id
    task_id = ti.task_id
    execution_date = context['execution_date']
    try_number = ti.try_number

    log_url = ti.log_url

    # log_text = message or read_task_log_file(context)

    hook = PostgresHook(postgres_conn_id='nbu_postgres')
    engine = hook.get_sqlalchemy_engine()

    insert_query = text("""
        INSERT INTO etl_logs (dag_id, task_id, execution_date, try_number, status, message)
        VALUES (:dag_id, :task_id, :execution_date, :try_number, :status, :message)
    """)

    with engine.begin() as conn:
        conn.execute(insert_query, {
            'dag_id': dag_id,
            'task_id': task_id,
            'execution_date': execution_date,
            'try_number': try_number,
            'status': status,
            'message': log_url
        })


def log_etl_success(context):
    print("[DEBUG] log_etl_success called")
    log_etl_event(context, status='success')


def log_etl_failure(context):
    log_etl_event(context, status='failure')

