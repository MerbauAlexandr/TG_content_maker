# src/data/add_users_akkaunts_info.py
# Этот файл добавляет и обновляет запись о базе данных users_akkaunts

from flask_sqlalchemy import SQLAlchemy
from config.config import app  # Правильный путь к файлу config.py
from flask_sqlalchemy import SQLAlchemy
from database_setup import DatabasesInfo, db


# Функция для удаления записи о базе данных users_akkaunts
def delete_users_akkaunts_info():
    db.session.query(DatabasesInfo).filter_by(database_id=2).delete()
    db.session.commit()
    print("Запись о базе данных users_akkaunts удалена.")


# Функция для добавления записи о базе данных users_akkaunts
def add_users_akkaunts_info():
    database_info = DatabasesInfo(
        database_id=2,
        database_name="users_akkaunts",
        database_description="База данных хранит информацию о пользователях приложения, включая данные для входа, каналы, назначенные роли и предпочтения по частоте публикаций.",
        database_usage="Используется для управления аккаунтами пользователей, их каналами и ролями. Ассистенты могут обращаться к этой базе для получения данных о пользователе, чтобы настроить персонализированный контент или провести взаимодействие с каналами."
    )

    db.session.add(database_info)
    db.session.commit()
    print("Обновлённая запись о базе данных users_akkaunts успешно добавлена.")


if __name__ == '__main__':
    with app.app_context():
        delete_users_akkaunts_info()  # Удаляем старую запись
        add_users_akkaunts_info()  # Добавляем обновлённую запись
