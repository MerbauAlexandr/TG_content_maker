# C:\Users\Pavlu4ini\PycharmProjects\TG_content_maker\create_all_databases.py

import sqlite3
import json
import os


# Функция для создания базы данных на основе JSON-описания
def create_database_from_json(json_file, db_folder):
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            db_structure = json.load(file)

        database_name = db_structure.get('database_name')
        variables = db_structure.get('variables', [])

        if not database_name:
            print(f"Ошибка: В файле {json_file} отсутствует ключ 'database_name'. Пропускаем этот файл.")
            return

        # Создаём папку, если она не существует
        if not os.path.exists(db_folder):
            os.makedirs(db_folder)

        # Путь к базе данных в папке 'data'
        db_path = os.path.join(db_folder, f'{database_name}.db')

        # Создаем базу данных
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Формируем SQL-запрос для создания таблицы
        create_table_query = f"CREATE TABLE IF NOT EXISTS {database_name} ("
        fields = []

        for var in variables:
            field = f"{var['name']} {var['type'].upper()}"

            # Добавляем ограничения, если есть
            if 'constraints' in var:
                # Пропускаем строки с `foreign key`, чтобы избежать ошибки
                if 'foreign key' in var['constraints'].lower():
                    continue
                field += f" {var['constraints']}"

            fields.append(field)

        create_table_query += ", ".join(fields) + ")"

        # Выполняем запрос на создание таблицы
        try:
            cursor.execute(create_table_query)
        except sqlite3.OperationalError as e:
            print(f"Ошибка при создании таблицы {database_name}: {e}")

        conn.commit()
        conn.close()

        print(f"База данных '{database_name}' успешно создана в папке {db_folder}!")

    except json.JSONDecodeError as e:
        print(f"Ошибка чтения файла {json_file}: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка при обработке файла {json_file}: {e}")


# Функция для поочередного создания всех баз данных на основе JSON-файлов
def create_all_databases_from_json():
    # Путь к JSON-файлам и к базе данных
    json_dir = r'C:\Users\Pavlu4ini\PycharmProjects\TG_content_maker\JSON'
    db_folder = r'C:\Users\Pavlu4ini\PycharmProjects\TG_content_maker\data'

    # Проверяем, существует ли директория с JSON-файлами
    if not os.path.exists(json_dir):
        print(f"Папка с JSON-файлами не найдена: {json_dir}")
        return

    json_files = [file for file in os.listdir(json_dir) if file.endswith('.json')]

    if not json_files:
        print(f"В папке {json_dir} не найдено JSON-файлов.")
        return

    for json_file in json_files:
        create_database_from_json(os.path.join(json_dir, json_file), db_folder)


# Запуск создания всех баз данных
if __name__ == "__main__":
    create_all_databases_from_json()
