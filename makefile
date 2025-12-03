# Устанавливаем переменные
UV = uv
PROJECT_NAME = config

# Установка зависимостей
install:
	$(UV) add

# Запуск Django сервера
runserver:
	$(UV) run python manage.py runserver

# Запуск Celery worker
celery:
	$(UV) run celery -A $(PROJECT_NAME) worker --loglevel=info

# Применение миграций
migrate:
	$(UV) run python manage.py makemigrations
	$(UV) run python manage.py migrate

# Запуск тестов
tests:
	$(UV) run pytest -v

# Полная сборка: установка + миграции
setup: install migrate

# Очистка pycache
clean:
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -exec rm -f {} +

# Комбинированная команда для разработки
dev: migrate runserver
