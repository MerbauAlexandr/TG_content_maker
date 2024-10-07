# config/config.py
# Этот файл отвечает за конфигурацию приложения

from flask import Flask
import os

app = Flask(__name__)

# Настройки для подключения к базе данных SQLite
# Полный путь к базе данных
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "../data/databases_info.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# API ключи
OPENAI_API_KEY = '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'  # Укажи свой API ключ OpenAI
NEWSAPI_KEY = '2cdec9820d1e40238696e591d75f3448'  # Укажи свой API ключ для NewsAPI
TELEGRAM_API_ID = 23541267  # Укажи свой API ID Telegram
TELEGRAM_API_HASH = '6c1ae024bf9e1375b0eb3627ec7978d7'  # Укажи свой API Hash Telegram
SESSION_FILE_PATH = 'data/session_name'  # Путь к файлу сессии Telegram
