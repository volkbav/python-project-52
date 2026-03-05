Для разворачивания приложения на сервере нужно выполнить следующие шаги:
## 1. Подготовка окружения
1.1. скопируйте файл `/env_examples/env_prod_example`:
```
cp env_examples/env_prod_example .env
```
1.2. Откорректируйте полученный файл (см. комментарии в файле) 
```
nano .env
``` 
1.3. Скорректируйте файл docker-compose.prod.yaml
```
nano docker-compose.prod.yaml
```
Нужно заменить в строчках
```
command: >
      certonly --webroot --webroot-path=/var/www/certbot
      --email example@example.com --agree-tos --no-eff-email
      -d example.com -d www.example.com
```
`--email example@example.com`, `-d example.com -d www.example.com` на ваш домен.

## 2. Получение сертификата для ssl
2.1. Скопируйте файл `nginx/default_create_ssl.conf` в `nginx/default.conf`
```
cp nginx/default_create_ssl.conf nginx/default.conf
```
2.2. Замените `example.com` в файле `nginx/default.conf` на ваш домен  
```
nano nginx/default.conf
```
2.3. Запустите nginx, db, backend для получения сертификата:
```
docker compose -f docker-compose.prod.yaml up -d db backend nginx
```
2.4. Проверьте, что nginx запустился с правильной конфигурацией
```
docker compose -f docker-compose.prod.yaml ps
```
Должны  увидеть `UP` у каждого контейнера  
2.5. Проверьте, что nginx действительно использует правильный конфиг
```
docker compose -f docker-compose.prod.yaml exec nginx cat /etc/nginx/conf.d/default.conf
```
2.6. Проверьте доступ к nginx 
```
curl -I http://localhost
```
Должен вернуть 502 Bad Gateway или 200 OK (если бэкенд уже запущен и ответил). Любой ответ, кроме 'Connection refused', означает, что nginx работает.  

2.7. Получение сертификата
```
docker compose -f docker-compose.prod.yaml run --rm certbot
```
2.8 Проверьте создание сертификата
```
ls -la ./certbot/certbot_etc/live/example.com/
```
2.9 Проверьте успешность получения сертификата
```
docker compose -f docker-compose.prod.yaml logs certbot
```
Должно быть "Success!"
## 3. Запуск приложения
3.1. Замените конфигурацию `nginx/default.conf`
```
cp nginx/default_example.conf nginx/default.conf
```
3.2. Отредактируйте файл `./nginx/default.conf`:
```
nano ./nginx/default.conf
```
замените в файлы адрес домена <example.com> и <www.example.com> на адрес вашего сайта.  
3.3. Перезапустите приложения:
```
docker compose -f docker-compose.prod.yaml down
```
```
docker compose -f docker-compose.prod.yaml up -d db backend nginx
```
3.4. Проверьте работу HTTPS
```
curl -I https://example.com
```
## 4. Обновление приложения
4.1. Для обновдения скачайте новый образ:
```
docker pull volkbav/task_manager
```
4.2. Пересоберите приложение:
```
docker compose -f docker-compose.prod.yaml build backend
```
4.3. Перезапустите приложение
```
docker compose -f docker-compose.prod.yaml down
```
```
docker compose -f docker-compose.prod.yaml up -d db backend nginx
```
# 5. Автообновление сертификатов
Добавьте в crontab:
```
0 0 * * * cd /путь/к/проекту && docker compose -f docker-compose.prod.yaml run --rm certbot
```
# 6. Проверка логов при проблемах
Если что-то пошло не так, смотрите логи:
```
docker compose -f docker-compose.prod.yaml logs nginx
```
```
docker compose -f docker-compose.prod.yaml logs backend
```
```
docker compose -f docker-compose.prod.yaml logs certbot
```