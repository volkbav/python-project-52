FROM python:3.13-slim

WORKDIR /app

RUN apt-get update \ 
    && apt-get install -y gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv

COPY . .

RUN uv sync

# копируем проект в образ
COPY . .
# удалить после сборки compose:
RUN uv run python manage.py collectstatic --noinput \
    && uv run python manage.py migrate

# открываем порт
EXPOSE 8000
# команды запуска контейнера
CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
