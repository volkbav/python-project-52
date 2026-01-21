FROM python:3.12-trixie

WORKDIR /usr/src/app
COPY . .
RUN build.sh


EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
