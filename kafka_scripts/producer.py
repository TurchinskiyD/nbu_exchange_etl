from kafka_scripts import KafkaProducer
import json
import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)

TOPIC = config['kafka_scripts']['topic']
BOOTSTRAP_SERVERS = config['kafka_scripts']['bootstrap_servers']


def publish_to_kafka(data: list):
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    for entry in data:
        producer.send(TOPIC, value=entry)

    producer.flush()
    producer.close()