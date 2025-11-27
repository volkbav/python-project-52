
build:
	./build.sh
.PHONY: build

collectstatic:
	uv run python manage.py collectstatic --noinput
.PHONY: collectstatic

install:
	uv sync
.PHONY: install

fix_lint:
	uv run ruff check --fix .
.PHONY: fix_lint

lint:
	uv run ruff check .
PHONY: lint

migrate:
	uv run python manage.py migrate
.PHONY: migrate

render-start:
	gunicorn task_manager.wsgi
.PHONY: render-start

repl:
	uv run manage.py shell
.PHONY: repl

start:
	uv run python manage.py runserver 0.0.0.0:8000
.PHONY: start

test:
	uv run pytest --cov=task_manager --cov-report=xml
.PHONY: test