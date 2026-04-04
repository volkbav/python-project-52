# Task Manager — Система управления задачами на Django

[![Tests](https://github.com/volkbav/python-project-52/actions/workflows/my_tests.yml/badge.svg)](https://github.com/volkbav/python-project-52/actions)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=volkbav_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=volkbav_python-project-52)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=volkbav_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=volkbav_python-project-52)

## 📋 Описание проекта

Task Manager — это веб-приложение для управления задачами, разработанное в рамках курса по Python-разработке. Приложение позволяет:

- Создавать, редактировать и удалять задачи
- Назначать статусы задач (To Do, In Progress, Done)
- Добавлять метки (labels) к задачам
- Управлять пользователями системы
- Фильтровать задачи по различным параметрам

## 🛠 Технологии

| Технология | Описание |
|------------|----------|
| **Django** | Высокоуровневый Python фреймворк для веб-разработки |
| **uv** | Современный менеджер пакетов и проектов (альтернатива pip) |
| **PostgreSQL** | Реляционная база данных |
| **Docker & Docker Compose** | Контейнеризация приложения |
| **Ruff** | Быстрый линтер и форматер кода |
| **Rollbar** | Трекинг ошибок и мониторинг качества |

## 📦 Структура проекта

```
task_manager/           # Основной Django проект
├── tasks/              # Модели, формы, представления задач
├── statuses/           # Управление статусами задач
├── labels/             # Управление метками
└── users/              # Управление пользователями
```

## 🚀 Быстрый старт (Docker)

### Требования

- Docker 20+ 
- Docker Compose 2.0+

### Запуск

1. **Создайте файл конфигурации:**
   ```bash
   cp .env_example .env
   ```

2. **Настройте переменные окружения** в файле `.env` (см. описание ниже)

3. **Запустите контейнеры:**
   ```bash
   docker compose up -d --build
   ```

4. **Доступ к сервисам:**
   - Приложение: http://localhost:8000
   - Администрирование БД (Adminer): http://localhost:8080

### Управление контейнерами

```bash
# Просмотр логов
docker compose logs -f backend
docker compose logs -f db

# Остановка без удаления данных
docker compose down

# Полная очистка (удаление всех томов)
docker compose down -v
```

## 🔧 Переменные окружения (.env)

| Переменная | Описание | Пример |
|------------|----------|--------|
| `POSTGRES_USER` | Имя пользователя БД | `taskmanager_user` |
| `POSTGRES_PASSWORD` | Пароль БД | `secure_password` |
| `POSTGRES_DB` | Имя базы данных | `task_manager_db` |
| `SECRET_KEY` | Секретный ключ Django | (генерируется автоматически) |
| `DEBUG` | Режим отладки | `True`/`False` |

## 📋 Локальная установка (без Docker)

### 1. Установка Python и uv

**macOS:**
```bash
brew install python3
brew install uv
```

**Linux (Ubuntu):**
```bash
sudo apt install python3 python3-venv
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Клонирование и установка зависимостей

```bash
git clone https://github.com/volkbav/python-project-52.git
cd python-project-52
make install
```

### 3. Настройка базы данных

Создайте файл `.env` на основе `.env_example`, затем:

```bash
# Запуск миграций
uv run python manage.py migrate

# Сбор статических файлов
uv run python manage.py collectstatic --noinput

# Создание суперпользователя
uv run python manage.py createsuperuser

# Запуск сервера
uv run python manage.py runserver 0.0.0.0:8000
```

## 🧪 Тестирование

```bash
make test
```

## 🔍 Лinting и форматирование

```bash
make lint      # Проверка кода через Ruff
make format    # Форматирование кода
```

## 📝 Development workflow

1. Вносите изменения в код — они сразу видны без пересборки контейнера
2. Используйте `docker compose logs -f backend` для просмотра ошибок
3. Adminer доступен по адресу http://localhost:8080 для управления БД

## ⚠️ Известные проблемы и troubleshooting

| Проблема | Решение |
|----------|---------|
| Ошибка подключения к БД | Проверьте переменные в `.env`, убедитесь что `db` запустился (`docker compose ps`) |
| Статические файлы не грузятся | Выполните `uv run python manage.py collectstatic --noinput` внутри контейнера |
| Порт 8000 занят | Измените маппинг портов в docker-compose.yaml или освободите порт |

## 📄 Документация

- [Docker Compose документация](docker_compose/README.md) — детальное описание конфигурации Docker
- [Production setup](docker_compose/README_prod.md) — настройка для продакшена

## 📜 Лицензия

Учебный проект в рамках курса Python Developer от Hexlet.

---

*Проект находится в разработке и может изменяться.*