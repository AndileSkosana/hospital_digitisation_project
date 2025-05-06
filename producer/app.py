import time
import random
import json
from kafka import KafkaProducer
from datetime import datetime
from utils import generate_random_patient_data
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
PG_HOST = os.getenv("PG_HOST")

# Kafka setup
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Stream data every 3 minutes
def stream_data():
    while True:
        patient_data = generate_random_patient_data()
        print(f"Sending data: {patient_data}")
        producer.send('hospital-data-topic', value=patient_data)
        time.sleep(180)  # 3 minutes

if __name__ == "__main__":
    stream_data()
