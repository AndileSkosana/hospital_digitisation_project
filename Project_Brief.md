
# Data Engineering: Hospital Digitisation Project

## Overview

Welcome to your first project as a data engineer – congratulations on reaching this milestone ⭐️!

You’ve just joined a consulting firm that’s been awarded a contract to digitise and consolidate hospital records for a major public hospital in Johannesburg. Your role is critical to this transformation. You’ll be working on streaming and batch ingestion of hospital records and helping update a modern data warehouse.

This project will simulate real-world data engineering scenarios involving data ingestion, data cleaning, and real-time database updates.

Your team lead wants to assess your technical abilities with this challenge over the next **9 days**. You’ve got this! 💪

## Project Tasks

### Task-1: Patient & Staff Generator

#### Instructions 🧑‍🏫
You will work with scripts that generate the core dataset of patients and hospital staff. These files must be produced ahead of time and used in all downstream ingestion pipelines.

#### Resources 📕

Code:
- `generate_people_data.py`
- `generate_staff_doctors.py`
- `assign_hospital_staff.py`

Learning Material:
- South African ID number format
- Age-based logic for staff assignment and retirement
- Data integrity for demographic and clinical data

#### Assessments ⏱
- Generated `people.csv` file with 5 million synthetic people.
- Assigned doctors and staff with specialty and shift logic.
- Replacements triggered when staff reach age 65.

---

### Task-2: Streaming & Batch Processing

#### Instructions 🧑‍🏫
Simulate streaming (every 3 minutes) and batch (every 15 minutes) data ingestion. You will use Kafka, PostgreSQL, and temporary storage to process new medical records.

#### Resources 📕

Code:
- `stream_producer.py`
- `batch_ingest.py`
- `docker-compose.yml`
- `init_db.sql`

Learning Material:
- Kafka Basics and Docker Networking
- Batch vs Streaming Ingestion Patterns
- PostgreSQL Best Practices for Warehousing

#### Assessments ⏱
- Streamed 3 new medical transfer events every 3 minutes.
- Processed daily patient record batches every 15 minutes.
- Maintained a 9-day ingestion window.
- Ensured total processed data size was approximately 5GB.

---

## Deliverables Checklist

Include the following in your final zip file upload:

- `people.csv`
- `hospital_patients.csv`
- `assigned_staff.csv`
- `docker-compose.yml`
- `README.md`
- `project_brief.pdf`
- All Python scripts in `producer/`, `consumer/`, and `database/` folders

---

## FAQ ❓

This section will be updated to include common setup or ingestion issues. For any bugs or errors, log an issue with your teaching assistant or code reviewer.

Best of luck with this challenge! 🚀
