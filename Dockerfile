FROM python:3.13-slim

WORKDIR /app

# не знаю почему, но без README uv sync падает
# вроде бы это из-за того, что он прописан, как обязательный в puproject.toml
COPY pyproject.toml uv.lock README.md ./

RUN pip install uv
RUN uv sync
# копируем проект в образ
COPY . .

# открываем порт - нужно только для остальных разработчиков
# порт будет назначаться через docker-compose
EXPOSE 8000

# эта команда будет переназначена в docker-compose (можно будет удалить)
CMD [ "uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]