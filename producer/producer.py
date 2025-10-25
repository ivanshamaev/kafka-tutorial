import json
import time
from kafka import KafkaProducer
from datetime import datetime

# Конфигурация продюсера
producer = KafkaProducer(
    bootstrap_servers=['172.40.0.1:9092'],  # Адрес брокера Kafka
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Сериализация сообщений в JSON
)

# Имя топика
TOPIC_NAME = "test-topic"

def main():
    try:
        for counter in range(10):
            message = {
                "message": f"Test message #{counter}",
                "timestamp": datetime.now().isoformat(),
                "counter": counter
            }
            
            # Отправляем сообщение
            future = producer.send(TOPIC_NAME, value=message)
            # Ждем подтверждения отправки
            record_metadata = future.get(timeout=10)
            
            print(f"Sent message #{counter}")
            
            # Ждем 1 секунду перед отправкой следующего сообщения
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping producer...")
    finally:
        # Закрываем продюсер
        producer.flush()
        producer.close()

if __name__ == "__main__":
    main()

