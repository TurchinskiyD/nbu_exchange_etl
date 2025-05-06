from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError
import json
import yaml

with open('config/config.yaml') as f:
    config = yaml.safe_load(f)

TOPIC = config['kafka']['topic']
BOOTSTRAP_SERVERS = config['kafka']['bootstrap_servers']
NUM_PARTITIONS = 1  # змінити за потребою
REPLICATION_FACTOR = 1


def create_kafka_topic():
    admin_client = KafkaAdminClient(bootstrap_servers=BOOTSTRAP_SERVERS)
    topic = NewTopic(name=TOPIC, num_partitions=NUM_PARTITIONS, replication_factor=REPLICATION_FACTOR)

    try:
        admin_client.create_topics(new_topics=[topic], validate_only=False)
        print(f"✅ Kafka topic '{TOPIC}' created with {NUM_PARTITIONS} partitions.")
    except TopicAlreadyExistsError:
        print(f"ℹ️ Kafka topic '{TOPIC}' already exists.")
    finally:
        admin_client.close()


def publish_to_kafka(data: list):
    create_kafka_topic()  # гарантує наявність партиційованого топіка

    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks = 'all'
    )

    for entry in data:
        if not isinstance(entry, dict) or "cc" not in entry or "rate" not in entry:
            print(f"Невалідне повідомлення, не відправлено: {entry}")
            continue
        producer.send(TOPIC, value=entry)

    producer.flush()
    producer.close()