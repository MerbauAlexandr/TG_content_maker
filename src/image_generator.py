# src/image_generator.py

import openai
from config.config import OPENAI_API_KEY

# Установка API-ключа OpenAI
openai.api_key = OPENAI_API_KEY  # Задаем API ключ

# Системный промт для ассистента
SYSTEM_PROMPT = (
    "Ты выполняешь роль промтинженера. Как профессионал, ты пишешь промты для получения высококачественных изображений для постов и сторис в Telegram. "
    "Изображения всегда должны быть:\n"
    "- Высокого разрешения.\n"
    "- Квадратными для постов и вертикальными для сторис.\n"
    "- Фотографичными и гиперреалистичными.\n\n"
    "При создании промтов учитывай следующие параметры:\n"
    "- **Экспозиция**: Убедись, что изображение хорошо освещено и сбалансировано.\n"
    "- **Фокусировка**: Главное внимание должно быть сосредоточено на основном объекте изображения, с размытым фоном для создания эффекта глубины.\n"
    "- **Качество**: Изображения должны иметь четкие детали и богатую цветовую палитру, чтобы привлечь внимание зрителей."
)

# Функция для генерации изображений
def generate_images(prompt_square, prompt_vertical):
    # Генерация квадратного изображения
    prompt_with_system_square = f"{SYSTEM_PROMPT}\n\nПромт для квадратного изображения: {prompt_square}"  # Добавляем системный промт к пользовательскому
    response_square = openai.Image.create(  # Запрос на создание квадратного изображения с OpenAI
        prompt=prompt_with_system_square,
        n=1,
        size="1024x1024",
    )
    image_url_square = response_square['data'][0]['url']  # Получаем URL сгенерированного квадратного изображения

    # Генерация вертикального изображения
    prompt_with_system_vertical = f"{SYSTEM_PROMPT}\n\nПромт для вертикального изображения: {prompt_vertical}"  # Добавляем системный промт к пользовательскому
    response_vertical = openai.Image.create(  # Запрос на создание вертикального изображения с OpenAI
        prompt=prompt_with_system_vertical,
        n=1,
        size="1024x1792",
    )
    image_url_vertical = response_vertical['data'][0]['url']  # Получаем URL сгенерированного вертикального изображения

    return image_url_square, image_url_vertical  # Возвращаем URL обоих изображений
