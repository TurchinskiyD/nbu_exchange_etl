from airflow.providers.postgres.hooks.postgres import PostgresHook
from sqlalchemy import text


def save_rates_to_postgres(rates: list, conn_id: str = 'nbu_postgres'):
    """
    Записуємо список курсів валют у PostgreSQl
    """
    if not rates:
        raise ValueError("No rates provided")

    hook = PostgresHook(postgres_conn_id=conn_id)
    engine = hook.get_sqlalchemy_engine()

    with engine.begin() as conn:
        for rate in rates:
            conn.execute(text
            ("""
                INSERT INTO exchange_rates (r030, ccy, txt, base_ccy, rate, exchangedate, date)
                VALUES (:r030, :ccy, :txt, :base_ccy, :rate, :exchangedate, now())
                ON CONFLICT (ccy, date) DO NOTHING
            """), {
                'r030': rate['r030'],
                'ccy': rate['cc'],
                'txt': rate['txt'],
                'base_ccy': rate['base_ccy'],
                'rate': rate['rate'],
                'exchangedate': rate['exchangedate']
            })