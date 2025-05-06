# Script to extract staff and assign specialties to doctors
import random
from datetime import datetime, timedelta
import pandas as pd
from faker import Faker

# Initialize Faker for generating random data
fake = Faker()

# Configuration
NUM_STAFF = 1000  # Number of staff members to generate (this includes doctors)
OUTPUT_FILE = "/data/staff.csv"

# List of possible specialities for doctors
specialties = ['Cardiologist', 'Surgeon', 'Pediatrician', 'Neurologist', 'Orthopedist', 'Dermatologist']

# Function to generate a single staff record
def generate_staff(is_doctor=False):
    age = random.randint(25, 65) if is_doctor else random.randint(18, 65)
    name = fake.first_name()
    surname = fake.last_name()
    staff_id = fake.unique.random_number(digits=6)
    gender = random.choice(['Male', 'Female'])
    role = 'Doctor' if is_doctor else 'Nurse'
    
    # Calculate hire date and assign a shift (randomly) for staff
    hire_date = fake.date_this_century()
    shift = random.choice(['Morning', 'Afternoon', 'Night'])
    
    # If the staff is a doctor, assign a specialty
    specialty = random.choice(specialties) if is_doctor else None

    staff = {
        'Staff_ID': staff_id,
        'Name': name,
        'Surname': surname,
        'Gender': gender,
        'Age': age,
        'Role': role,
        'Specialty': specialty,
        'Hire_Date': hire_date.strftime('%Y-%m-%d'),
        'Shift': shift,
        'Staff_Assigned_To': fake.company(),
        'Status': 'Active' if age < 65 else 'Retired'  # Staff member retires after 65
    }

    return staff

# Generate doctors and non-doctors
staff_data = [generate_staff(is_doctor=True) for _ in range(NUM_STAFF // 2)] + \
             [generate_staff(is_doctor=False) for _ in range(NUM_STAFF // 2)]

df = pd.DataFrame(staff_data)
df.to_csv(OUTPUT_FILE, index=False)
