from airflow.providers.postgres.hooks.postgres import PostgresHook
from sqlalchemy import text


def log_etl_event(context, status: str, message: str = None):
    """

    :param context:
    :param status:
    :param message:
    :return:
    """
    ti = context['task_instance']
    dag_id = context['dag'].dag_id
    task_id = ti.task_id
    execution_date = context['execution_date']
    try_number = ti.try_number

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
            'message': message or ''
        })


def log_etl_success(context):
    log_etl_event(context, status='success')


def log_etl_failure(context):
    log_etl_event(context, status='failure', message=str(context.get('exception', '')))