# src/telegram_bot.py

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config.config import TELEGRAM_API_ID, TELEGRAM_API_HASH, SESSION_FILE_PATH

# Создаём экземпляр бота
bot = Bot(token=TELEGRAM_API_HASH)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет, мир!")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
