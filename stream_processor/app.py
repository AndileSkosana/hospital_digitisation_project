from kafka import KafkaConsumer
import json
from utils import process_patient_data
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
PG_HOST = os.getenv("PG_HOST")

# Kafka setup
consumer = KafkaConsumer(
    'hospital-data-topic',
    bootstrap_servers=['kafka:9092'],
    group_id='stream-processor-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def process_data():
    for message in consumer:
        patient_data = message.value
        print(f"Processing data: {patient_data}")
        process_patient_data(patient_data)

if __name__ == "__main__":
    process_data()
