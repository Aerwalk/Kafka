
import json
import mysql.connector
from kafka import KafkaConsumer, KafkaProducer

db = mysql.connector.connect(
    host='mysql-db:33060',
    user='root',
    password='123456',
    database='restaurant_reviews'
)
cursor = db.cursor()

# Создание Kafka Consumer для чтения данных из Kafka
consumer = KafkaConsumer('raw_data', bootstrap_servers='kafka:9092')

# Создание Kafka Producer для отправки сообщений в Kafka
producer = KafkaProducer(bootstrap_servers='kafka:9092')

# Функция для обработки сообщений из Kafka
def process_kafka_message(message):
    data = json.loads(message.value.decode('utf-8'))

    if 'review_id' in data and 'user_id' in data and 'restaurant_id' in data and 'rating' in data:
        review_id = data['review_id']
        user_id = data['user_id']
        restaurant_id = data['restaurant_id']
        rating = data['rating']

        # Добавление нового отзыва в базу данных
        add_review_query = "INSERT INTO reviews (review_id, user_id, restaurant_id, rating) VALUES (%s, %s, %s, %s)"
        cursor.execute(add_review_query, (review_id, user_id, restaurant_id, rating))
        db.commit()

        print(f"Добавлен новый отзыв: Review ID - {review_id}, User ID - {user_id}, Restaurant ID - {restaurant_id}, Rating - {rating}")

        # Отправка сообщения в Kafka после успешного добавления записи в базу данных
        result = {
            'review_id': review_id,
            'status': 'success'
        }
        producer.send('processed_data', json.dumps(result).encode('utf-8'))
        producer.flush()

    else:
        print("Неверный формат данных из Kafka")

# Чтение данных из Kafka и обработка
for message in consumer:
    process_kafka_message(message)