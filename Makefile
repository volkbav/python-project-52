
build:
	./build.sh

.PHONY: build

install:
	uv sync

.PHONY: install

fix_lint:
	uv run ruff check --fix .

PHONY: fix_lint

render-start:
	gunicorn task_manager.wsgi

.PHONY: render-start

start:
	uv run manage.py runserver 0.0.0.0:8000

.PHONY: start

