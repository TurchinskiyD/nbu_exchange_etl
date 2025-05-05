from airflow.providers.postgres.hooks.postgres import PostgresHook


def create_exchange_rates_table():
    hook = PostgresHook(postgres_conn_id='nbu_postgres')
    """
    Створюємо таблицю exchange_rates, якщо вона ще не існує.
    """
    create_query = """
    CREATE TABLE IF NOT EXISTS exchange_rates (
        r030 NUMERIC,
        ccy VARCHAR(5),
        txt TEXT,
        base_ccy VARCHAR(3),
        rate NUMERIC,
        exchangedate DATE,
        date TIMESTAMP DEFAULT now(),
        PRIMARY KEY (ccy, date)
    );
    """
    hook.run(create_query)


def create_etl_logs_table(conn_id: str = 'nbu_postgres'):
    create_query = """
    CREATE TABLE IF NOT EXISTS etl_logs (
        log_time TIMESTAMP DEFAULT now(),
        dag_id TEXT,
        task_id TEXT,
        execution_date TIMESTAMP,
        try_number INTEGER,
        status TEXT,
        message TEXT
    );
    """
    hook = PostgresHook(postgres_conn_id=conn_id)
    hook.run(create_query)