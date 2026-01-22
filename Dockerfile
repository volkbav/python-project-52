FROM python:3

WORKDIR /usr/src/app

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*
RUN pip install uv


COPY pyproject.toml uv.lock ./
RUN uv sync

COPY . .


EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
