# nbu_exchange_etl

ETL-процес для автоматизованого збору, обробки та зберігання курсів валют із НБУ за допомогою Apache Airflow, Apache Kafka, PostgreSQL та Python.

## Архітектура
Airflow DAG 

↓ (щоденний запит)

API НБУ (JSON)

   ↓

Kafka Producer (topic: nbu_exchange_rates)

   ↓

Kafka Consumer (Python)

   ↓

PostgreSQL (таблиця exchange_rates)


## Компоненти
**1. Airflow**

* DAG nbu_exchange_rates_to_db виконує:
* перевірку доступності API НБУ
* отримання та відправку даних у Kafka
* зчитування з Kafka
* збереження у PostgreSQL
* логування статусів

**2. Kafka**

* Producer публікує курси в топік nbu_exchange_rates
* Consumer читає ці дані та вставляє їх у БД

**3. PostgreSQL**

* Таблиця exchange_rates з первинним ключем (ccy, exchangedate)
* Таблиця etl_logs для логування статусів DAG/тасків

## Налаштування
* Запусти docker-compose.yaml (Kafka + PostgreSQL + Airflow)
* Створи підключення nbu_postgres, nbu_api в UI Airflow
* Створити файли .env та config для передачі даних для підключення

![dag.png](images%2Fdag.png)
