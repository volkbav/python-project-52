FROM nginx:1.29.6

RUN useradd -s /bin/sh -m devuser
WORKDIR /app
# меняем владельца рабочей директории (без этого uv не работает)
RUN chown -R devuser:devuser /app

COPY ./default.conf /etc/nginx/conf.d/default.conf