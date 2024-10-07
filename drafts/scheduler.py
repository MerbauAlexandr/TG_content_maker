# src/scheduler.py

import schedule
import time
from datetime import datetime
from threading import Thread
from database import get_all_posts  # Импортируем функцию для получения постов

# Функция для публикации постов
def publish_posts():
    posts = get_all_posts()  # Получаем все посты из базы данных
    for post in posts:
        title, description, content, scheduled_time = post[1], post[2], post[3], post[4]  # Извлекаем данные поста
        if scheduled_time <= datetime.now():  # Проверяем, нужно ли публиковать пост
            print(f"Публикация поста: {title}")  # Здесь добавим логику для публикации поста
            # Логика публикации поста в Telegram

# Функция для запуска планировщика
def run_scheduler():
    schedule.every(1).minutes.do(publish_posts)  # Запускаем функцию каждые 1 минуту
    while True:
        schedule.run_pending()  # Выполняем запланированные задачи
        time.sleep(1)  # Задержка на 1 секунду

# Функция для запроса информации о группе и роли
def plan_content():
    group = input("Для какой группы планируется контент-план? ")  # Запрашиваем группу
    role = input("От имени какой роли будет генерироваться контент? ")  # Запрашиваем роль
    print(f"Контент будет запланирован для группы '{group}' от имени роли '{role}'.")  # Подтверждение выбора

# Запуск планировщика в отдельном потоке
def start_scheduler():
    thread = Thread(target=run_scheduler)  # Создаем новый поток
    thread.start()  # Запускаем поток
