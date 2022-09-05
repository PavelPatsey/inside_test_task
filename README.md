# Проект inside_test_task

![inside_test_task workflow](https://github.com/PavelPatsey/inside_test_task/actions/workflows/main.yml/badge.svg)

Реализация тестового задания на позицию Junior Developer. Описание задания находится по адресу ./Junior_Developer_task_description.txt, можно посмотреть по [ссылке](https://github.com/PavelPatsey/inside_test_task/blob/main/Junior_Developer_task_description.txt).

## Стек технологий

- проект написан на Python с использованием Django REST Framework;
- база данных - PostgreSQL;
- система управления версиями - git;
- [Docker](https://docs.docker.com/engine/install/ubuntu/), [Dockerfile](https://docs.docker.com/engine/reference/builder/).

## Реализовано

- Кастомная JWT аутентификация.
- Требуемые в задании эндпоинты.
- GitHub Actions:
    - Проверка кода на соответствие PEP8 и выполнение тестов, реализованных в проекте.
    - Сборка и публикация образа приложения на DockerHub.

## Образ Docker
Образ Docker находится в репозитории по адресу:
https://hub.docker.com/repository/docker/pavelpatsey/inside_project

## Запуск проекта с помощью Dockerfile:

1. Склонируйте репозиторий.
2. Перейдите в директорию ./inside_project, в которой находится Dockerfile.
3. Соберите образ:
 ```
docker build -t inside_project .
 ```
4. Запустите контейнер:
```
docker run -d --name inside_api -it -p 8000:8000 inside_project
```
## Запуск проекта с помощью образа из Dockerhub:

1. Скачайте образ:
 ```
docker image pull pavelpatsey/inside_project:1
 ```
2. Запустите контейнер:
```
docker run -d --name inside_api_pulled -it -p 8000:8000 pavelpatsey/inside_project:1
```

## Endpoints:

### Аутентификация пользователя.
`http://localhost:8000/api/auth/token/`\
POST запрос с телом вида:
```json
{
  "name": "имя отправителя",
  "password": "пароль"
}
```
В случае удачной аутентификации возвращает JWT токен:
```json
{
  "token": "xxxxx.xxxx.xxxx"
}
```
### Заголовок Authorization.
Формат заголовка "Authorization" должен быть таким:\
"Bearer_token"

### Отправка сообщения или запрос истории. 
`http://localhost:8000/api/messages/`\
POST запрос с телом вида:
```json
{
  "name": "имя отправителя",
  "message": "новое сообщение"
}
```
В ответ получает:
```json
{
  "name": "имя отправителя",
  "message": "новое сообщение"
}
```
В случае, если отправлен POST запрос вида:
```json
{
  "name": "user_name",
  "message": "history n"
}
```
где n - целое неотрицательное число, возвращает последние n из БД.
Например, если n равно 5 в ответ получает:
```json
[
    {"name": "имя отправителя", "message": "новое сообщение"},
    {"name": "имя отправителя", "message": "test message text 14"},
    {"name": "имя отправителя", "message": "test message text 13"},
    {"name": "имя отправителя", "message": "test message text 12"},
    {"name": "имя отправителя", "message": "test message text 11"},
]
```
## Curl

Файл с примерами запросов находится по адресу ./curl_commands, можно посмотреть по [ссылке](https://github.com/PavelPatsey/inside_test_task/blob/main/curl_commands). Должны быть установлены curl и jq, если нет:
```
apt install curl
apt install jq
```
