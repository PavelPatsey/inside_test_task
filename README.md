# Проект inside_test_task

![inside_test_task workflow](https://github.com/PavelPatsey/inside_test_task/actions/workflows/main.yml/badge.svg)

Реализация тестового задания на позицию Junior Developer. Описание задания находится по адресу ./task_description/Junior_Developer_task_description.txt

## Стек технологий

- проект написан на Python с использованием Django REST Framework;
- база данных - PostgreSQL;
- система управления версиями - git;
- [Docker](https://docs.docker.com/engine/install/ubuntu/), [Dockerfile](https://docs.docker.com/engine/reference/builder/), [Docker Compose](https://docs.docker.com/compose/).

## Реализовано

- Кастомная JWT аутентификация.
- Требуемые в задании POST эндпоинты.
- GitHub Actions:
    - Проверка кода на соответствие PEP8 и выполнение тестов, реализованных в проекте.
     - Сборка и публикация образа приложения на DockerHub.

## Образ Docker
Образ Docker находится в репозитории по адресу:
https://hub.docker.com/repository/docker/pavelpatsey/inside_project

## Запуск проекта в Докере:

1. Склонируйте репозиторий.
2. В каталоге ./infra создайте файл .env c аналогичной структурой:
 ```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=password_postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
SECRET_KEY=django_secret_key # секретный ключ django (установите свой)
 ```
3. В командной строке перейдите в папку ./infra, запустите docker-compose в фоновом режиме командой:
```
docker-compose up -d
```
4. Примените миграции:
```
docker-compose exec web python manage.py migrate

```
5. Чтобы зайти в админку создайте суперпользователя:
```
docker-compose exec web python manage.py createsuperuser

```
Теперь проект доступен по адресу http://localhost/api/messages/

Админка доступна по адресу http://localhost/admin/

6. Чтобы протестировать работу приложения заполните БД тестовыми данными:

```
docker-compose exec backend python3 manage.py fill_database_with_test_data
```
Файл с примерами запросов находится по адресу ./curl_commands
