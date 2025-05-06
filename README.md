# Hospital Digitisation Project - README

## 📘 Overview
This project simulates a digital hospital environment through synthetic data generation and real-time/batch data streaming. The system includes infrastructure for data generation, streaming via Kafka, batch ingestion, and storage in a shared lake environment.

---

## 🧱 Infrastructure Components
The project runs on **8 Docker containers**:

1. **Kafka** – Event streaming platform.
2. **Zookeeper** – Coordinates Kafka brokers.
3. **PostgreSQL** – Stores ingested batch data.
4. **pgAdmin** – GUI to interact with PostgreSQL.
5. **Producer** – Publishes synthetic transfer/patient data to Kafka.
6. **Stream Processor** – Consumes Kafka stream data.
7. **Batch Ingestor** – Periodically ingests batch files to the database.
8. **Scheduler** – Coordinates timed data generation and ingestion.

---

## 🗃️ Shared Volume / Data Lake
A shared volume simulates a data lake where records land in two separate folders:
- `lake/batch/` — Daily batch files
- `lake/stream/` — Real-time transfer files

---

## ⏱️ Simulation Logic
- **Simulation Period:** December 1, 2020 – March 31, 2025 (1455 days)
- **Compression Ratio:** 9 real-world days = 1455 simulated days
- **Batch Logic:** Every **15 minutes** = **1 simulated day** of batch data
- **Stream Logic:** Every **3 minutes** = **3 transfer records**
  - Every 5th stream aligns with the current batch day

---

## 📦 Project Structure
```bash
├── configs/                     # Kafka, DB, and shift configuration
├── producer/                    # Producers for batch and stream data
├── scripts/                     # Data generation scripts
├── docs/                        # Project brief and marking rubric
└── README.md                    # This file
```

---

## 🚀 How to Run

### 1. Build and Start Containers
```bash
docker-compose up --build
```

### 2. Generate Data
Run these scripts manually or via the scheduler:
```bash
python scripts/generate_people_csv.py
python scripts/generate_doctors.py
python scripts/generate_hospital_patients.py
python scripts/generate_staff_assignments.py
```

### 3. Stream and Ingest Data
```bash
python producer/stream_transfers_producer.py
python producer/batch_patient_data_producer.py
```

---

## ⚙️ Configuration
Update the following as needed:
- `configs/kafka_config.json`
- `configs/database_config.json`
- `configs/hospital_shift_config.json`

---

## ✅ Deliverables
- Generated synthetic data (CSV)
- Kafka logs
- Lake folder structure (`batch/`, `stream/`)
- PostgreSQL database entries

---

## ❗ Common Issues
- Kafka not connecting? Check Docker logs and `bootstrap_servers`.
- Stream or batch delays? Verify your simulation timing setup.
- Permission denied? Ensure volume mounts are accessible and Python has write access.

---

## 🙋 Questions?
Refer to `project_brief.md` or contact your instructor/supervisor.
