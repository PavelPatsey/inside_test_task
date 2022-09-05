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
- Требуемые в задании POST эндпоинты.
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
docker run --name inside_api -it -p 8000:8000 inside_project
```
## Запуск проекта с помощью образа, скаченного из Dockerhub:

1. Склонируйте репозиторий.
2. Скачайте образ:
 ```
docker image pull pavelpatsey/inside_project:1
 ```
4. Запустите контейнер:
```
docker run -d --name inside_api_pulled -it -p 8000:8000 pavelpatsey/inside_project:1
```

## Endpoints

Проект доступен по адресу http://localhost/api/

## Curl

Файл с примерами запросов находится по адресу ./curl_commands, можно посмотреть по [ссылке](https://github.com/PavelPatsey/inside_test_task/blob/main/curl_commands). Должны быть установлены curl и jq, если нет:
```
apt install curl
apt install jq
```
