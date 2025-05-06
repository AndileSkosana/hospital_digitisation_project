import time
from apscheduler.schedulers.background import BackgroundScheduler
from producer.app import stream_data
from batch_ingestor.app import ingest_batch_data
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
PG_HOST = os.getenv("PG_HOST")
scheduler = BackgroundScheduler()

# Add jobs to run every 3 minutes (for the producer) and every 15 minutes (for the batch ingestor)
scheduler.add_job(stream_data, 'interval', minutes=3)
scheduler.add_job(ingest_batch_data, 'interval', minutes=15)

if __name__ == "__main__":
    scheduler.start()
    try:
        # Run the scheduler forever
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
