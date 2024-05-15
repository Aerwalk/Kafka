-- Создаем базу данных, если ее еще нет
CREATE DATABASE IF NOT EXISTS restaurant_reviews;

USE restaurant_reviews;

-- Создаем таблицу restaurants, если ее еще нет
CREATE TABLE IF NOT EXISTS restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

