🚀 Быстрый запуск

1. Активируй виртуальное окружение
venv\Scripts\activate

2. Настрой pre-commit
pip install black isort flake8
активация в терминале(если нужно):
black .
flake8 .
isort .

3. Установи зависимости
pip install -r requirements.txt

4. Настрой базу данных
Создай БД PostgreSQL (например, real_db)
Проверь подключение в .env или в коде (если хардкод)

5. Запусти бота в app/main.py
