# src/text_overlay.py

from PIL import Image, ImageDraw, ImageFont

# Функция для наложения текста на изображение
def overlay_text(image_path, text, output_path):
    image = Image.open(image_path)  # Открываем изображение
    draw = ImageDraw.Draw(image)  # Создаем объект для рисования

    # Настройки текста
    font_size = 40  # Размер шрифта
    font = ImageFont.load_default()  # Используем шрифт по умолчанию

    # Позиция текста (центрирование)
    text_width, text_height = draw.textsize(text, font=font)  # Получаем размеры текста
    position = ((image.width - text_width) // 2, image.height - text_height - 20)  # Центрируем текст

    # Наносим текст на изображение
    draw.text(position, text, (255, 255, 255), font=font)  # Белый цвет текста
    image.save(output_path)  # Сохраняем изображение с наложенным текстом
