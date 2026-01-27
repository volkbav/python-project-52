FROM python:3.13-slim

WORKDIR /app

RUN apt-get update \ 
    && apt-get install -y gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv


COPY pyproject.toml uv.lock ./
RUN uv sync

# копируем проект в образ
COPY . .

# выполняем миграции и собираем статические файлы (если нужно)
# RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# открываем порт
EXPOSE 8000
# команды запуска контейнера
CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
