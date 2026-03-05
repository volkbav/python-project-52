Для разворачивания приложения на сервере нужно выполнить следующие шаги:
## 1 Подготовка окружения
1.1 скопируйте файл `/env_examples/env_prod_example`:
```
cp /env_examples/env_prod_example .env
```
1.2 Откорректируйте полученный файл (см. комментарии в файле)  

## 2 Получение сертификата для ssl
2.1 Скопируйте файл `nginx/default_create_ssl.conf` в `nginx/default.conf`
```
cp nginx/default_create_ssl.conf nginx/default.conf
```
2.2 Замените `example.com` в файле `nginx/default.conf` на ваш домен  
2.3 Запустите nginx для получения сертификата:
```
docker compose -f docker-compose.prod.yaml up -d nginx
```

  3. Отредактируйте файл `./nginx/default.conf`:
- замените в файлы адрес домена <example.com> и <www.example.com> на адрес вашего сайта
4. Скорректируйте docker-compose.prod для получения сертификата (certbot) - адрес почты и сайта
4. запустите докер:
```
docker compose -f docker-compose.prod.yaml -d up
```
env_examples/env_prod_example