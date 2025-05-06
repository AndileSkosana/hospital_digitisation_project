# Script to generate 5 million synthetic people
import random
import pandas as pd
from faker import Faker

# Initialize Faker for generating random data
fake = Faker()

# Configuration
NUM_PEOPLE = 5000000  # Number of people to generate
OUTPUT_FILE = "/data/people.csv"

# Function to generate a single person record
def generate_person():
    # Randomly generating demographic data for each person
    person = {
        'ID': fake.unique.random_number(digits=6),
        'Name': fake.first_name(),
        'Surname': fake.last_name(),
        'Gender': random.choice(['Male', 'Female']),
        'Date_of_Birth': fake.date_of_birth(minimum_age=18, maximum_age=100).strftime('%Y-%m-%d'),
        'Race': random.choice(['Black', 'White', 'Indian', 'Coloured']),
        'ID_Number': fake.unique.random_number(digits=13),
        'Address': fake.address(),
        'Phone_Number': fake.phone_number(),
    }
    return person

# Generate people and save to a CSV file
people_data = [generate_person() for _ in range(NUM_PEOPLE)]
df = pd.DataFrame(people_data)
df.to_csv(OUTPUT_FILE, index=False)
