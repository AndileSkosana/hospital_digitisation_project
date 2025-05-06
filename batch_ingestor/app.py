import time
import random
from utils import generate_batch_data, insert_batch_into_db
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
PG_HOST = os.getenv("PG_HOST")

# Simulate batch record every 15 minutes
def ingest_batch_data():
    while True:
        batch_data = generate_batch_data()
        print(f"Ingesting batch data: {batch_data}")
        insert_batch_into_db(batch_data)
        time.sleep(900)  # 15 minutes

if __name__ == "__main__":
    ingest_batch_data()
