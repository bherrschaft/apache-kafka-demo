
Apache Kafka Demo: Transaction Producer and Consumer
This project demonstrates how to create a Kafka producer to send text messages to a topic and a Kafka consumer to read those messages. The example simulates bank transactions and processes them using Kafka.

Prerequisites
Docker: Ensure you have Docker installed on your machine. Install Docker
Python: Python 3.8 or higher installed on your machine. Install Python
Anaconda (recommended): To manage your Python environment. Install Anaconda
Kafka-Python: Kafka client for Python. This will be installed via the virtual environment.
Project Setup
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/apache-kafka-demo.git
cd apache-kafka-demo
Set Up the Python Environment

Create a virtual environment using Conda:
bash
Copy code
conda create --name kafka-env python=3.8
conda activate kafka-env
Install the necessary Python packages:
bash
Copy code
pip install kafka-python
Start Kafka Using Docker

Ensure Docker is running.
Navigate to your project directory and start Kafka:
bash
Copy code
docker-compose up -d
Verify that the Kafka and Zookeeper containers are running:
bash
Copy code
docker ps
Create a Kafka topic for transactions:
bash
Copy code
docker exec -it <kafka-container-id> /opt/kafka/bin/kafka-topics.sh --create --topic bank-transactions --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
Run the Kafka Producer and Consumer

In one terminal window, run the producer:
bash
Copy code
python transaction_producer.py
In another terminal window, run the consumer:
bash
Copy code
python transaction_consumer.py
Shut Down Kafka

To stop the Kafka services when you're done:
bash
Copy code
docker-compose down
Project Structure
transaction_producer.py: Sends simulated bank transactions to the Kafka topic.
transaction_consumer.py: Reads and processes the transactions from the Kafka topic.
docker-compose.yml: Configuration file for Docker to set up Kafka and Zookeeper.
How to Start and Stop Kafka
Start Kafka:
bash
Copy code
docker-compose up -d
Stop Kafka:
bash
Copy code
docker-compose down
Notes
Ensure that your Python environment is activated (conda activate kafka-env) when running the producer and consumer scripts.
The project is configured to run in a development environment. Adjust the Docker and Python settings for production use as needed.
License
This project is licensed under the MIT License.

