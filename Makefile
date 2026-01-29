
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

messages:
	uv run django-admin makemessages -l ru
.PHONY: messages

migrate:
	uv run python manage.py makemigrations
	uv run python manage.py migrate
.PHONY: migrate

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
	uv run coverage run --source='.' manage.py test
	uv run coverage xml
	uv run coverage report --show-missing
.PHONY: test

test_django:
	uv run manage.py test
.PHONY: test_django

test_with_coverage:
	uv run coverage run --source='.' manage.py test
	uv run coverage xml
.PHONY: test_with_coverage

docker-build:
	docker compose up -d --build
.PHONY: docker-build