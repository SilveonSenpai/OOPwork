import json
import os

class Storage:
    """Клас для збереження та завантаження даних у JSON-файли."""

    def __init__(self, file_path):
        self.file_path = file_path

    def save_data(self, data):
        """Зберігає дані у JSON-файл."""
        try:
            with open(self.file_path, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        """Завантажує дані з JSON-файлу."""
        if not os.path.exists(self.file_path):
            return []  # Якщо файл не існує, повертаємо порожній список
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading data: {e}")
            return []

