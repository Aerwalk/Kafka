import time
from flask import Flask, request, jsonify
import requests
from kafka import KafkaProducer, KafkaConsumer
import json
import threading

app = Flask(__name__)
time.sleep(10)
producer = KafkaProducer(bootstrap_servers='kafka:9092')
consumer = KafkaConsumer('processed_data', bootstrap_servers='kafka:9092', group_id='api-service-group')

def send_data_to_kafka(data):
    producer.send('raw_data', value=json.dumps(data).encode('utf-8'))

def get_processed_data_from_kafka():
    data_list = []
    for message in consumer:
        data_list.append(json.loads(message.value.decode('utf-8')))
    return data_list

@app.route('/send_review', methods=['POST'])
def send_review():
    data = request.json
    send_data_to_kafka(data)
    return 'Review sent to data service for processing...'

@app.route('/get_processed_reviews', methods=['GET'])
def get_processed_reviews():
    processed_data = get_processed_data_from_kafka()
    return jsonify(processed_data)

if __name__ == '__main__':
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()