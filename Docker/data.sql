-- Создаем таблицу reviews, если ее еще нет
CREATE TABLE IF NOT EXISTS reviews (
    id INT PRIMARY KEY,
    restaurant_id INT,
    review_text TEXT,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
);
-- Добавление тестовых данных в таблицу "restaurants"
INSERT INTO restaurants (id, name) VALUES (1, 'Ресторан А'),
                                          (2, 'Ресторан Б'),
                                          (3, 'Ресторан В');

-- Добавление тестовых данных в таблицу "reviews"
INSERT INTO reviews (id, restaurant_id, review_text) VALUES
(1, 1, 'Отличный ресторан с вкусной кухней.'),
(2, 1, 'Обслуживание было медленным, но еда была вкусная.'),
(3, 2, 'Превосходное обслуживание и атмосфера.'),
(4, 3, 'Не впечатлил, не рекомендую.');