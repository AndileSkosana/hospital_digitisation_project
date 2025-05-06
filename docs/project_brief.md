# Hospital Data Digitization Project Walkthrough

## Overview

Welcome to the Hospital Data Digitization Project! In this project, you will simulate the digitalization of a state hospital’s medical records. The hospital records contain data that needs to be streamed and stored in real-time. You’ll implement a system where both real-time streaming and batch data are processed and stored in a hospital records database over a 9-day period. This project involves working with multiple containers, including Kafka, PostgreSQL, and a custom producer for medical data. You will also simulate hospital staff assignments and patient records, ensuring data integrity and efficient storage.

### Key Technologies Used:
Docker & Docker Compose

Kafka (for streaming)

PostgreSQL (for batch processing)

Python (for scripting and data generation)

VS Code (for development)

## Step-by-Step Walkthrough
### Step 1: Project Setup
Clone the Repository (if provided):

Clone the project repository or extract the project zip that contains all the necessary files, including the docker-compose.yml, Python scripts, and additional assets.

#### Ensure Prerequisites:

Ensure Docker and Docker Compose are installed on your machine.

Make sure Python 3.x and the necessary libraries (like pandas, faker, kafka-python, etc.) are installed.

### Step 2: Docker Setup
Start the Containers:

In your project folder (where docker-compose.yml is located), open a terminal and run the following command:

bash
Copy
Edit
docker-compose up --build
This command will start all the required containers, including:

Kafka for streaming data

PostgreSQL for storing batch data

Other supporting services like Zookeeper, pgAdmin, Producer, etc.

Verify Containers:

Check that all the containers are running correctly by running:

bash
Copy
Edit
docker ps
You should see a list of all running containers, including kafka, postgres, and other services.

### Step 3: Data Generation and Streaming
Data Generation:

The producer script generates synthetic hospital patient and staff data. This includes patient information, diagnosis, treatment, and hospital staff details like specialty and shifts.

It also assigns staff to the hospital based on their specialty and age. Staff are reassigned or replaced after they reach 65.

Running the Producer:

The producer script will simulate streaming data into Kafka every 3 minutes (for medical transfers) and batch data every 15 minutes (representing a day’s worth of records).

You can monitor the generated data by accessing the logs for the producer container.

### Step 4: Data Storage
Streaming Data (Kafka):

The producer sends the generated medical data into Kafka.

Kafka streams are consumed by other services for further processing (like data storage or analytics).

Batch Data (PostgreSQL):

The batch ingestion system collects data every 15 minutes and stores it in PostgreSQL.

Batch data represents records like new patient admissions, updates to patient statuses, and doctor assignments.

Database Management:

You can use pgAdmin to manage and view the data stored in PostgreSQL. Simply connect to the PostgreSQL container via the pgAdmin web interface.

### Step 5: Accessing Logs and Debugging
Viewing Logs:

You can view logs from any of the containers using the docker logs command:

bash
Copy
Edit
docker logs <container_name>
For example, to view logs from the producer container:

bash
Copy
Edit
docker logs producer
Handling Errors:

Ensure all services are connected correctly (Kafka and PostgreSQL). If there are any errors, check the Docker logs for more information.

### Step 6: Finalizing and Storing the Data
Data Validation:

After running the system for the 9-day period, validate that data has been correctly streamed and stored in the database.

Ensure that the data is consistent across both real-time and batch records.

Exporting Data:

Once the data is complete, you can export the data from PostgreSQL to CSV or other formats for further analysis.

### Step 7: Shutting Down the Containers
Stopping the Containers:

After completing your task, stop the Docker containers by running:

bash
Copy
Edit
docker-compose down

Project Brief Recap
You are a data engineer at a company contracted to digitize the hospital records of a major state hospital. The existing data starts from 2020, and new data will be streamed in every 3 minutes, while batch records will be processed every 15 minutes. The task is to store the streamed and batch files, update the database, and ensure that the data is accurately ingested over a 9-day period, totaling approximately 5GB of data.

## Key Points:
Streaming every 3 minutes: 3 new records will be streamed.

Batch processing every 15 minutes: This will represent one day of hospital records.

Data Size: The total data volume will be around 5GB.

9-day duration: The project will simulate 9 days of hospital records updates.

Good Luck! 🚀
This walkthrough document provides a detailed guide on how to set up and complete the project. 