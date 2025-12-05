
build:
	./build.sh
.PHONY: build

collectstatic:
	uv run python manage.py collectstatic --noinput
.PHONY: collectstatic

translate:
	uv run django-admin compilemessages
.PHONY: translate

install:
	uv sync
.PHONY: install

fix_lint:
	uv run ruff check --fix .
.PHONY: fix_lint

lint:
	uv run ruff check .
PHONY: lint

makemigrations:
	uv run python manage.py makemigrations
.PHONY: makemigrations

messages:
	uv run django-admin makemessages -l ru
.PHONY: messages

migrate:
	uv run python manage.py migrate
.PHONY: migrate

mm:
	make makemigrations
	make migrate
.PHONY: mm

render-start:
	gunicorn task_manager.wsgi
.PHONY: render-start

shell:
	uv run manage.py shell
.PHONY: shell

start:
	uv run python manage.py runserver 0.0.0.0:8000
.PHONY: start

test:
	uv run pytest --cov=task_manager --cov-report=xml
.PHONY: test

test_django:
	uv run manage.py test
.PHONY: test_django