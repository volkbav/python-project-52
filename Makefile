
build:
	./build.sh

.PHONY: build

render-start:
	gunicorn task_manager.wsgi

.PHONY: render-start

start:
	uv run manage.py runserver 0.0.0.0:8000

.PHONY: start