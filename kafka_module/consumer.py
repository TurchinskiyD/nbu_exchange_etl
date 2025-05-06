from kafka import KafkaConsumer
from kafka.errors import KafkaError
from airflow.exceptions import AirflowSkipException
import json
import yaml


with open('config/config.yaml') as f:
    config = yaml.safe_load(f)


TOPIC = config['kafka']['topic']
BOOTSTRAP_SERVERS = config["kafka"]["bootstrap_servers"]


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

        data = [msg.value for msg in consumer]

        if not data:
            raise AirflowSkipException('Нових повідомлень немає, зупиняємо Dag')

        consumer.commit()
        consumer.close()

        return data
    except KafkaError as e:
        raise Exception(f'KafkaError: {str(e)}')
