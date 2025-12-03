## Деплой проекта через Docker

### Необходимые сервисы

* Django + DRF
* Celery worker
* PostgreSQL
* Redis (брокер Celery)

Всё это уже описано в `docker-compose.yml`.

---

### Запуск

1. Собрать образы:

```bash
docker-compose build
```

2. Создать и запустить контейнеры:

```bash
docker-compose up -d
```

* Django будет доступен на `http://localhost:8000`
* Celery worker подключен к Redis и выполняет асинхронные задачи
* PostgreSQL и Redis запускаются как отдельные сервисы
---

### Миграции и подготовка БД

```bash
docker-compose run web uv run python manage.py migrate
```

При необходимости можно создать суперпользователя:

```bash
docker-compose run web uv run python manage.py createsuperuser
```

---

### Тесты и проверки

```bash
docker-compose run web uv run pytest -v
```

---

### Особенности продакшн

* Для продакшн лучше использовать **Gunicorn/Uvicorn + Nginx** вместо встроенного `runserver`
 
```bash
docker-compose run web uv run gunicorn config.asgi:application --workers 4 --bind 0.0.0.0:8000
```
Предварительно настроив Nginx для проекта.
* Также стоит использовать PostgreSQL и Redis в системе, а не в контейнере.

Самым лучшим решением будет настроить Pipeline CI/CD в Gitlab, установив несколько stages, где будут:
1. Сборка проекта(dockerfile)
2. Прогон тестов
3. Запуск на проде