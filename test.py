import requests

# Отправка отзыва для обработки
review_data = {
    'review_id': 12,
    'user_id': 1,
    'restaurant_id': 1,
    'rating': 5
}

response = requests.post('http://localhost:8080/send_review', json=review_data)
print(response.text)

# Получение обработанных данных
response = requests.get('http://localhost:8080/get_processed_reviews')
processed_data = response.json()
print(processed_data)