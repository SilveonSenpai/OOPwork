# Game Management System with Console Interface

## Опис проєкту

**Game Management System** — це консольний додаток для управління персонажами та зброєю у вигляді текстової гри. Додаток взаємодіє з **API**, обробляє отримані дані і зберігає їх локально у форматі JSON.

---

## Функціонал

- 📋 **Оновлення списку персонажів та зброї** з API.
- 📝 **Перегляд деталей персонажів та предметів**.
- 🎮 **Створення нових персонажів** через консольний інтерфейс.
- 📊 **Система станів персонажа** та управління інвентарем.
- 🔄 **Збереження та відновлення стану гри**.

---

## Структура проєкту

```plaintext
game_project/
├── api_client.py       # API-клієнт для запитів
├── characters.py       # Класи персонажів
├── cli2.py             # Логіка команд CLI
├── data_parser.py      # Обробка даних із API
├── items.py            # Класи предметів
├── logger.py           # Журналювання подій
├── main.py             # Головний файл для запуску програми
├── storage.py          # Робота з локальним сховищем
├── test_game.py        # Тести
└── text_renderer.py    # Генерація текстового представлення
```

---

## Встановлення та запуск

### **1. Клонування репозиторію**

```bash
git clone https://github.com/your-username/game_project.git
cd game_project
```

### **2. Встановлення залежностей**

Переконайтеся, що Python 3.9+ встановлено. Встановіть необхідні бібліотеки:
```bash
pip install requests
```

### **3. Запуск додатка**

```bash
python main.py
```

---

## Приклади використання

### **Оновлення персонажів**
```plaintext
Updating character list...
Successfully updated and saved 85 characters.
```

### **Показ деталей персонажа**
```plaintext
Available Characters:
1. Albedo
2. Amber
3. Ayaka

Choose a character by number: 1

Character Details:
Name: Albedo
Health: 100
Armor: 20
Attack: 30
Description: A genius alchemist from Mondstadt.
Image URL: https://link-to-image
```

### **Створення нового персонажа**
```plaintext
Enter details for the new character:
Name: TestHero
Health: 150
Armor: 50
Attack: 40
Description: A custom hero created by the user.
Image URL (optional): https://example.com/testhero.png

New character 'TestHero' created and saved successfully!
```

---

## Тестування

Для запуску тестів використовуйте:
```bash
python -m unittest test_game.py
``` 