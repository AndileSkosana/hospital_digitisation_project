# Kafka producer to stream transfer records every 3 minutes
import random
from datetime import datetime, timedelta
import pandas as pd
from faker import Faker

# Initialize Faker for generating random data
fake = Faker()

# Configuration
NUM_STREAMS = 5  # Simulate 5 streams (example)
NUM_PATIENTS = 1000
OUTPUT_FILE = '/data/medical_stream.csv'

# Function to simulate medical data stream
def generate_medical_stream():
    stream_data = []
    for _ in range(NUM_STREAMS):
        for _ in range(NUM_PATIENTS):
            patient_data = {
                'Patient_ID': fake.unique.random_number(digits=6),
                'Name': fake.first_name() + " " + fake.last_name(),
                'Gender': random.choice(['Male', 'Female']),
                'Age': random.randint(0, 100),
                'Diagnosis': random.choice(['Flu', 'Pneumonia', 'Diabetes', 'Hypertension']),
                'Admit_Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'Discharge_Date': (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S'),
            }
            stream_data.append(patient_data)
    return stream_data

# Generate stream data
stream_data = generate_medical_stream()

# Convert to DataFrame and save to CSV
df = pd.DataFrame(stream_data)
df.to_csv(OUTPUT_FILE, index=False)
