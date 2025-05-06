from kafka import KafkaConsumer
from kafka.errors import KafkaError
from airflow.exceptions import AirflowSkipException
import json
import yaml


with open('config/config.yaml') as f:
    config = yaml.safe_load(f)


TOPIC = config['kafka']['topic']
BOOTSTRAP_SERVERS = config["kafka"]["bootstrap_servers"]
REQUIRED_FIELDS = {"r030", "cc", "txt", "base_ccy", "rate", "exchangedate"}


def read_from_kafka():
    try:
        consumer = KafkaConsumer(
            TOPIC,
            bootstrap_servers=BOOTSTRAP_SERVERS,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            auto_offset_reset='earliest',
            enable_auto_commit=False,
            consumer_timeout_ms=10000,
            group_id="airflow_consumer"
        )

        valid_data = []
        for msg in consumer:
            val = msg.value
            if not isinstance(val, dict) or not REQUIRED_FIELDS.issubset(val.keys()):
                print(f'Пропущено невалідне повідомлення: {val}')
            valid_data.append(val)

        if not valid_data:
            raise AirflowSkipException('Нових повідомлень немає, зупиняємо Dag')

        consumer.commit()
        consumer.close()

        return valid_data

    except KafkaError as e:
        raise Exception(f'KafkaError: {str(e)}')
