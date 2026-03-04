Для разворачивания приложения на сервере нужно выполнить следующие шаги:
1. скопировать `/env_examples/env_prod_example`:
```
cp /env_examples/env_prod_example .env
```
2. Откорректировать полученный файл
3. Отредактируйте файл `./nginx/default.conf`:
- замените в файлы адрес домена <example.com> и <www.example.com> на адрес вашего сайта
4. запустите докер:
```
docker compose up
```