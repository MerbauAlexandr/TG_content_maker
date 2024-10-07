# src/data/database_setup.py
# Этот файл отвечает за создание и инициализацию таблиц в базе данных

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../config')))

from config import app  # Импортируем объект app для SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# Таблица для хранения информации о базах данных
class DatabasesInfo(db.Model):
    __tablename__ = 'databases_info'
    database_id = db.Column(db.Integer, primary_key=True)
    database_name = db.Column(db.String(100), nullable=False)
    database_description = db.Column(db.Text, nullable=False)
    database_usage = db.Column(db.Text, nullable=False)
    variables = db.Column(db.JSON, nullable=False)  # Поле для хранения переменных в формате JSON

    def __repr__(self):
        return f"<Database {self.database_name}>"

# Создание всех таблиц
if __name__ == '__main__':
    with app.app_context():  # Добавляем контекст приложения
        db.create_all()
        print("Таблицы созданы.")
