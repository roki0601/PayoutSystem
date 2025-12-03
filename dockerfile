FROM ghcr.io/astral-sh/uv:python3.11-alpine

WORKDIR /app

COPY pyproject.toml uv.lock /app/
COPY config/ /app/config/
COPY modules/ /app/modules/
COPY manage.py /app/

RUN uv add

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
