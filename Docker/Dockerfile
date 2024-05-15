FROM mysql:latest

# Создание базы данных и таблиц с использованием SQL-скрипта
COPY init.sql /docker-entrypoint-initdb.d/
COPY data.sql /docker-entrypoint-initdb.d/
# Задаем переменные окружения для MySQL
ENV MYSQL_ROOT_PASSWORD=123456
ENV MYSQL_DATABASE=restaurant_reviews

# Публикация порта MySQL
EXPOSE 3306