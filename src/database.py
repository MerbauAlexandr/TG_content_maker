# src/database.py

import sqlite3

# Функция для инициализации базы данных пользователей
def initialize_user_database():
    conn = sqlite3.connect('data/users.db')  # Подключение к базе данных пользователей
    cursor = conn.cursor()  # Создание курсора

    # Создание таблицы для хранения пользователей и их информации
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id TEXT UNIQUE,
            session_token TEXT,
            channels TEXT,
            user_role TEXT,  -- Изменяем поле role на user_role
            posts_per_week INTEGER CHECK(posts_per_week BETWEEN 1 AND 7)
        )
    ''')
    conn.commit()  # Сохранение изменений
    conn.close()  # Закрытие подключения

# Функция для инициализации базы данных контент-плана
def initialize_content_plan_database():
    conn = sqlite3.connect('data/content_plan.db')  # Подключение к базе данных контент-плана
    cursor = conn.cursor()  # Создание курсора

    # Создание таблицы для хранения контент-плана
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS content_plan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            channel TEXT,
            title TEXT,
            meta_description TEXT,
            post_content TEXT,  -- Добавляем поле для содержания поста
            inspirational_quote TEXT,  -- Добавляем поле для вдохновляющей цитаты
            scheduled_date DATETIME,
            publication_date DATETIME,
            image_url_square TEXT,  -- Ссылка на квадратное изображение
            image_url_vertical TEXT,  -- Ссылка на вертикальное изображение
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()  # Сохранение изменений
    conn.close()  # Закрытие подключения
