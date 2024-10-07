# src/main.py

import uvicorn
from fastapi import FastAPI
from telegram_bot import app as telegram_app  # Импортируем приложение Telegram
from content_generator import app as content_app  # Импортируем приложение генерации контента

# Создание экземпляра FastAPI
app = FastAPI()

# Встраивание других приложений
app.mount("/telegram", telegram_app)  # Встраиваем Telegram-бота
app.mount("/content", content_app)  # Встраиваем генератор контента

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Запускаем приложение
