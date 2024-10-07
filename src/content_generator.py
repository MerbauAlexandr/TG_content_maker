# src/content_generator.py

import os
from fastapi import FastAPI
from pydantic import BaseModel
import openai
import requests
from config.config import OPENAI_API_KEY

# Создание экземпляра FastAPI
app = FastAPI()

# Установка API-ключа OpenAI
openai.api_key = OPENAI_API_KEY  # Задаем API ключ

# Определение модели для запроса темы
class Topic(BaseModel):
    topic: str
    role: str  # Добавляем поле для роли ассистента

# Функция для получения последних новостей по теме
def get_recent_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey=YOUR_NEWSAPI_KEY"  # Замените на ваш API ключ
    response = requests.get(url)
    articles = response.json()["articles"]  # Получаем статьи
    recent_news = [article["title"] for article in articles[:3]]  # Берем первые три статьи
    return "\n".join(recent_news)  # Возвращаем заголовки статей

# Функция для генерации поста
def generate_post(topic, role):
    recent_news = get_recent_news(topic)  # Получаем последние новости

    # Системный промт для ассистента
    SYSTEM_PROMPT = (
        f"Ты ассистент, который выполняет роль {role}. Ты профессионал своего дела и умеешь заинтересовать свою целевую аудиторию интересным контентом. "
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

    # Генерация юзерного промта для изображения
    user_prompt_square = f"Напиши короткое описание изображения, которое ты хотел бы разместить в качестве изображения для поста на тему '{title}' с метасообщением '{meta_description}'."  # Промт для квадратного изображения
    user_prompt_vertical = f"Напиши короткое описание изображения, которое ты хотел бы разместить в качестве анонса для поста на тему '{title}' с метасообщением '{meta_description}'."  # Промт для вертикального изображения

    # Генерация содержания поста
    prompt_post = f"{SYSTEM_PROMPT}\n\nНапишите подробный и увлекательный пост для блога на тему: {topic}, учитывая следующие последние новости:\n{recent_news}\n\nИспользуйте короткие абзацы, подзаголовки, примеры и ключевые слова для лучшего восприятия и SEO-оптимизации."  # Подготовка промта
    response_post = openai.ChatCompletion.create(  # Генерация поста с OpenAI
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_post}],
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )
    post_content = response_post.choices[0].message.content.strip()  # Получаем содержание поста

    return {
        "title": title,  # Возвращаем заголовок
        "meta_description": meta_description,  # Возвращаем мета-описание
        "post_content": post_content,  # Возвращаем содержание поста
        "user_prompt_square": user_prompt_square,  # Возвращаем юзерный промт для квадратного изображения
        "user_prompt_vertical": user_prompt_vertical  # Возвращаем юзерный промт для вертикального изображения
    }

# Эндпоинт для генерации поста
@app.post("/generate-post")
async def generate_post_api(topic: Topic):
    generated_post = generate_post(topic.topic, topic.role)  # Генерируем пост с учетом роли
    return generated_post  # Возвращаем сгенерированный пост

# Эндпоинт для проверки работоспособности API
@app.post("/heartbeat")
async def heartbeat_api():
    return "OK"  # Возвращаем статус
