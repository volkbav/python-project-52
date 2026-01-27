FROM python:3.13-slim

WORKDIR /app

RUN apt-get update \ 
    && apt-get install -y gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv
# не знаю почему, но без README uv sync падает
# вроде бы это из-за того, что он прописан, как обязательный в puproject.toml
COPY pyproject.toml uv.lock README.md ./

RUN uv sync
# копируем проект в образ
COPY . .
# удалить после сборки compose:
RUN uv run python manage.py collectstatic --noinput \
    && uv run python manage.py migrate

# открываем порт
EXPOSE 8000

