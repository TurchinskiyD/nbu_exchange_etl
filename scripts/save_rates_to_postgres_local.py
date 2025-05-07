from sqlalchemy import create_engine, text

import os

user = os.getenv("POSTGRES_USER", "airflow")
password = os.getenv("POSTGRES_PASSWORD", "airflow")
host = os.getenv("POSTGRES_HOST", "localhost")
port = os.getenv("POSTGRES_PORT", "5433")
db = os.getenv("POSTGRES_DB", "nbu_etl")


def save_rates_to_postgres_local(rates: list):
    if not rates:
        raise ValueError("No rates provided")

    # Підстав свій рядок підключення
    db_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    engine = create_engine(db_url)

    with engine.begin() as conn:
        for rate in rates:
            conn.execute(text("""
                INSERT INTO nbu.exchange_rates (r030, ccy, txt, base_ccy, rate, exchangedate, date)
                VALUES (:r030, :ccy, :txt, :base_ccy, :rate, :exchangedate, now())
                ON CONFLICT (ccy, exchangedate) DO NOTHING
            """), {
                'r030': rate['r030'],
                'ccy': rate['cc'],
                'txt': rate['txt'],
                'base_ccy': rate['base_ccy'],
                'rate': rate['rate'],
                'exchangedate': rate['exchangedate']
            })
