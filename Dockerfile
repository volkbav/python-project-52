FROM python:3.13-slim
# создаем пользователя для контейнера
RUN useradd -s /bin/sh -m devuser
WORKDIR /app
# меняем владельца рабочей директории (без этого uv не работает)
RUN chown -R devuser:devuser /app

# устанавливаем uv глобально
RUN pip install uv

USER devuser

# Создаём виртуальное окружение в директории проекта
RUN uv venv
ENV PATH="/app/.venv/bin:$PATH"

# README прописан, как обязательный в puproject.toml
COPY pyproject.toml uv.lock README.md ./

RUN uv sync
# # копируем проект в образ
COPY . .

# открываем порт - нужно только для остальных разработчиков
# порт будет назначаться через docker-compose
EXPOSE 8000

# эта команда будет переназначена в docker-compose (можно будет удалить)
CMD [ "uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]