# базовый образ
FROM python:3.12-slim

# Настройки Python
# не генерировать .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# логи сразу выводятся в Docker, а не буферизуются
ENV PYTHONUNBUFFERED=1 


# рабочая директория внутри контейнера
WORKDIR /app
# обновляем образ 
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libssl-dev \       
#    libjpeg-dev \
#    zlib1g-dev \      
    && rm -rf /var/lib/apt/lists/*

# libpq-dev - для работы PostgreSQL
# libjpeg-dev - Pillow (изображения)
# zlib1g-dev - Pillow

# устанавливаем uv
RUN pip install --no-cache-dir uv

# создаём виртуальное окружение
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# разворачиваем проект
COPY pyproject.toml .
RUN uv sync --python /opt/venv/bin/python

# копируем проект в образ
COPY . .

# выполняем миграции и собираем статические файлы (если нужно)
# RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# открываем порт
EXPOSE 8000
# команды запуска контейнера
CMD ["gunicorn", "task_manager.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
