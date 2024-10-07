# src/smm_assistant.py

import requests
import openai
from datetime import datetime, timedelta
from database import add_post_to_db  # Импортируем функцию для добавления поста в базу данных
from config.config import OPENAI_API_KEY

# Установка API-ключа OpenAI
openai.api_key = OPENAI_API_KEY  # Задаем API ключ

# Функция для получения последних новостей по теме
def get_recent_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey=YOUR_NEWSAPI_KEY"  # Замените на ваш API ключ
    response = requests.get(url)
    articles = response.json()["articles"]  # Получаем статьи
    recent_news = [article["title"] for article in articles[:3]]  # Берем первые три статьи
    return "\n".join(recent_news)  # Возвращаем заголовки статей

# Функция для генерации заголовка и мета-описания
def generate_post(topic, user_role):
    # Системный промт для ассистента
    SYSTEM_PROMPT = (
        f"Ты ассистент, который выполняет роль {user_role}. Ты профессионал своего дела и умеешь заинтересовать свою целевую аудиторию интересным контентом. "
        "Ты пишешь контент на русском языке, используешь минимальное количество эмоджи (4-7 на весь пост), "
        "даёшь короткие, но ёмкие примеры и в постах просказываешь тонкий юмор. "
        "Твоя задача — создавать привлекательные и информативные посты, которые будут вызывать интерес у читателей."
    )

    # Генерация заголовка поста
    prompt_title = f"{SYSTEM_PROMPT}\n\nПридумайте привлекательный заголовок для поста на тему: {topic}"  # Подготовка промта
    response_title = openai.ChatCompletion.create(  # Генерация заголовка с OpenAI
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_title}],
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    title = response_title.choices[0].message.content.strip()  # Получаем заголовок

    # Генерация мета-описания
    prompt_meta = f"{SYSTEM_PROMPT}\n\nНапишите краткое, но информативное мета-описание для поста с заголовком: {title}"  # Подготовка промта
    response_meta = openai.ChatCompletion.create(  # Генерация мета-описания с OpenAI
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_meta}],
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    meta_description = response_meta.choices[0].message.content.strip()  # Получаем мета-описание

    return title, meta_description  # Возвращаем заголовок и мета-описание

# Функция для создания контент-плана на месяц
def create_content_plan(user_id, channels, user_role, posts_per_week):
    topic = "Актуальные события"  # Задаем общую тему для постов
    for week in range(4):  # Генерация на 4 недели
        for post in range(posts_per_week):  # В зависимости от количества постов в неделю
            title, meta_description = generate_post(topic, user_role)  # Генерация заголовка и мета-описания
            scheduled_date = datetime.now() + timedelta(weeks=week, days=post)  # Запланированная дата публикации
            # Добавляем пост в базу данных
            add_post_to_db(user_id, channels, title, meta_description, scheduled_date, None, None, None)

