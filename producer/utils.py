import random
import json
from datetime import datetime

# Randomly generate patient data for streaming
def generate_random_patient_data():
    names = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"]
    conditions = ["Flu", "Pneumonia", "Asthma", "Diabetes", "Hypertension"]

    name = random.choice(names)
    condition = random.choice(conditions)
    admission_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    patient_data = {
        "id": random.randint(1000, 9999),
        "name": name,
        "condition": condition,
        "admission_date": admission_date
    }
    return patient_data

# Function to process the patient data (can be extended to save into DB or files)
def process_patient_data(patient_data):
    print(f"Processed Patient Data: {json.dumps(patient_data)}")

# Generate random batch data for ingestion
def generate_batch_data():
    batch_data = [generate_random_patient_data() for _ in range(random.randint(5, 10))]
    return batch_data

# Function to insert the batch data into a database (this would interact with a real database in production)
def insert_batch_into_db(batch_data):
    # Simulating database insertion by printing
    print(f"Inserting batch into DB: {json.dumps(batch_data)}")
