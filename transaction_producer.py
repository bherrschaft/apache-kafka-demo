# transaction_producer.py
from kafka import KafkaProducer
import json
import time

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Function to send transactions
def send_transaction(transaction):
    producer.send('bank-transactions', transaction)
    producer.flush()

# Example transactions
transactions = [
    {'account': '123456', 'amount': 250, 'currency': 'USD'},
    {'account': '654321', 'amount': 1000, 'currency': 'EUR'},
    {'account': '789012', 'amount': 500, 'currency': 'GBP'}
]

# Send transactions with a delay
for transaction in transactions:
    send_transaction(transaction)
    print(f"Sent: {transaction}")
    time.sleep(1)  # Wait 1 second between each message

producer.close()
