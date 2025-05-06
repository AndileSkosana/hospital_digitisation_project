# Kafka producer to stream batch patient records every 15 minutes
import random
import pandas as pd
from datetime import datetime, timedelta

# Configuration
NUM_BATCHES = 5  # Number of batches to simulate
NUM_PATIENTS_PER_BATCH = 100  # Patients per batch
OUTPUT_FILE = '/data/batch_data.csv'

# Function to simulate medical batch data
def generate_batch_data():
    batch_data = []
    for _ in range(NUM_BATCHES):
        for _ in range(NUM_PATIENTS_PER_BATCH):
            patient_data = {
                'Patient_ID': random.randint(100000, 999999),
                'Name': f'Patient{random.randint(1000, 9999)}',
                'Gender': random.choice(['Male', 'Female']),
                'Age': random.randint(0, 100),
                'Diagnosis': random.choice(['Flu', 'Pneumonia', 'Diabetes', 'Hypertension']),
                'Admit_Date': (datetime.now() - timedelta(days=random.randint(0, 10))).strftime('%Y-%m-%d'),
                'Discharge_Date': (datetime.now() + timedelta(days=random.randint(5, 10))).strftime('%Y-%m-%d'),
            }
            batch_data.append(patient_data)
    return batch_data

# Generate batch data
batch_data = generate_batch_data()

# Convert to DataFrame and save to CSV
df = pd.DataFrame(batch_data)
df.to_csv(OUTPUT_FILE, index=False)
