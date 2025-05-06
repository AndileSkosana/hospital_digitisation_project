Marking Rubric
1. Docker Setup and Configuration (25%)
25 points: Docker containers set up and configured correctly. All services (Kafka, Zookeeper, PostgreSQL, Producer, Stream Processor, Batch Ingestor, Scheduler) are running properly.

20 points: Docker setup works with minor issues (e.g., misconfigurations in environment variables).

15 points: Some containers are missing or not configured correctly.

10 points: Docker setup is incomplete or not working as expected.

2. Data Stream and Batch Simulation (30%)
30 points: Stream and batch records are simulated correctly over the 9-day period. Data aligns as expected, with 3-minute and 15-minute intervals for streaming and batch updates.

25 points: Stream and batch data is simulated but with minor misalignments or issues with timing.

20 points: Simulation runs but with significant errors or timing issues.

10 points: Stream or batch data is missing or does not run.

3. Data Storage and Management (20%)
20 points: Data is stored logically in the shared folder simulating a data lake. Batch and stream records are organized appropriately for future analysis.

15 points: Data is stored, but some organization issues (e.g., incorrect folder structure).

10 points: Data is stored but with major issues regarding organization or structure.

5 points: Data storage setup is incomplete or does not meet requirements.

4. Code Quality and Documentation (15%)
15 points: The code is well-structured, clean, and documented. Functions and variables are named appropriately, and the README and comments are comprehensive.

12 points: Code is mostly clean, with some documentation and naming issues.

10 points: Code is functional but lacks clear structure or documentation.

5 points: Code is hard to follow with little to no documentation.

5. Docker Compose File (10%)
10 points: The docker-compose.yml file is well-structured and properly configured for all services.

8 points: The docker-compose.yml file is functional but with minor issues.

5 points: The docker-compose.yml file is incomplete or contains major errors.

3 points: No docker-compose.yml file or it does not work.