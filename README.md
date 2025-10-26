# kafka-tutorial
```
kafka-tutorial/
├── docker-compose.yml     # Docker Compose config for Zookeeper, Kafka broker, Kafdrop
├── .gitignore             # Ignore rules for Python, Docker, IDE, etc.
├── producer/
│   └── producer.py        # Python producer: отправляет тестовые сообщения в Kafka
├── consumer/
│   └── consumer.py        # Python consumer: читает сообщения из Kafka
```

This repository contains a minimal Kafka tutorial setup using Docker Compose. It runs ZooKeeper, a single Kafka broker and Kafdrop (UI) so you can inspect topics and messages.

Quick overview:
- Start the cluster: `docker-compose up -d`
- Stop the cluster: `docker-compose down`
- Kafdrop UI: http://172.40.0.1:9000/ (or http://localhost:9000/ depending on your Docker network)

This project includes a simple Python producer at `producer/producer.py` which can send test messages to `test-topic` (topic must exist or be auto-created if enabled).

# Commands
```
docker-compose up -d
```

```
docker-compose down
```

# UI Kafdrop
UI Kafdrop доступен по адресу: http://172.40.0.1:9000/

# venv
```
python3 -m venv venv
source venv/bin/activate
pip install kafka-python
```

# Создаем топик
```
docker exec -it broker kafka-topics --create --topic test-topic --bootstrap-server broker:9092 --partitions 3 --replication-factor 1
```

# Запуск Producer

```
python producer/producer.py
```

# Запуск Consumer

```
python consumer/consumer.py
```
