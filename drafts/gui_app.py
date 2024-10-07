# src/gui_app.py

import tkinter as tk
from tkinter import messagebox
from telethon import TelegramClient, events
from config.config import TELEGRAM_API_ID, TELEGRAM_API_HASH, SESSION_FILE_PATH
import os

# Проверяем наличие папки data
if not os.path.exists('data'):
    os.makedirs('data')

# Создаем клиента Telethon
client = TelegramClient(SESSION_FILE_PATH, TELEGRAM_API_ID, TELEGRAM_API_HASH)

# Функция для создания окна приложения
def create_gui():
    window = tk.Tk()
    window.title("Telegram Content Maker")

    # Функция для авторизации
    def authorize():
        client.start()
        messagebox.showinfo("Статус", "Авторизация прошла успешно!")

    # Функция для отправки тестового сообщения
    async def send_test_message():
        await client.send_message('me', 'Hello from the Telegram Content Maker!')
        messagebox.showinfo("Статус", "Сообщение отправлено!")

    # Кнопка для авторизации
    auth_button = tk.Button(window, text="Авторизоваться", command=authorize)
    auth_button.pack(pady=10)

    # Кнопка для отправки тестового сообщения
    send_message_button = tk.Button(window, text="Отправить сообщение", command=lambda: client.loop.run_until_complete(send_test_message()))
    send_message_button.pack(pady=10)

    # Запуск графического интерфейса
    window.mainloop()

# Запуск приложения
if __name__ == '__main__':
    create_gui()
