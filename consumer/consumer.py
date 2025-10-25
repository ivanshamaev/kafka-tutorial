from kafka import KafkaConsumer
import json

TOPIC_NAME = "test-topic"
BOOTSTRAP_SERVERS = ["172.40.0.1:9092"]

# Создаем Kafka consumer
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='test-consumer-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
)

print(f"Listening for messages on topic '{TOPIC_NAME}'...")
try:
    for message in consumer:
        print(f"Received: {message.value}")
except KeyboardInterrupt:
    print("\nStopping consumer...")
finally:
    consumer.close()
