Kafka Transaction Processing Example
This project demonstrates how to use Apache Kafka to send and consume text messages. Specifically, it simulates a scenario where bank transactions are sent to a Kafka topic by a producer and consumed by a consumer.

Prerequisites
Before running this project, ensure you have the following installed on your system:

Docker: Used to run Kafka and Zookeeper in containers.
Docker Compose: Facilitates the setup of multi-container Docker applications.
Miniconda/Anaconda: Used to create and manage a Python virtual environment.
Python 3.7+: Ensure Python is installed for running the scripts.
Project Setup
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/apache-kafka-demo.git
cd apache-kafka-demo
2. Set Up and Activate the Python Virtual Environment
Create a virtual environment using conda:

bash
Copy code
conda create --name kafka-env python=3.8
conda activate kafka-env
Install the necessary Python dependencies:

bash
Copy code
pip install kafka-python six
3. Start Kafka and Zookeeper
Kafka requires Zookeeper to run. You can start both services using Docker Compose.

bash
Copy code
docker-compose up -d
4. Create a Kafka Topic
To create a Kafka topic named bank-transactions, run the following command:

bash
Copy code
docker exec -it <kafka-container-id> /opt/kafka/bin/kafka-topics.sh --create --topic bank-transactions --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
Replace <kafka-container-id> with the ID of your Kafka container, which you can find using docker ps.

5. Run the Kafka Producer
The producer sends messages (bank transactions) to the bank-transactions topic.

bash
Copy code
python transaction_producer.py
6. Run the Kafka Consumer
The consumer reads messages from the bank-transactions topic.

bash
Copy code
python transaction_consumer.py
7. Stopping Kafka and Zookeeper
Once you are done, you can stop Kafka and Zookeeper by bringing down the Docker containers:

bash
Copy code
docker-compose down
How It Works
Producer: Sends a series of bank transactions (as JSON objects) to the bank-transactions Kafka topic.
Consumer: Listens to the bank-transactions topic and processes the transactions as they arrive.
Key Files
docker-compose.yml: Configures and manages the Kafka and Zookeeper services using Docker.
transaction_producer.py: Contains the code for producing (sending) messages to Kafka.
transaction_consumer.py: Contains the code for consuming (reading) messages from Kafka.
Additional Notes
Make sure Docker is running before starting Kafka and Zookeeper.
If you encounter issues with the Python environment, double-check that you are using the correct virtual environment (kafka-env).