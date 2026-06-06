# Отчет по домашнему заданию ЛР8

## Источник задания

Лабораторная работа выполнена по репозиторию `tp-lessons/lab_docker`.

## Задание

Нужно подготовить web-приложение, которое сохраняет введенную задачу в базу данных, добавить Dockerfile и настроить `docker-compose.yml` для совместной работы приложения и MySQL.

## Что сделано

1. Добавлен каталог `app/` с Flask-приложением.
2. Добавлен файл `requirements.txt` с зависимостями.
3. Добавлен каталог `db/` и файл `db/init.sql` для создания таблицы `tasks`.
4. Добавлен `Dockerfile` для запуска Python-приложения.
5. Добавлен `docker-compose.yml` с сервисами `app` и `db`.
6. Для приложения открыт порт `5000`.
7. Для MySQL добавлены healthcheck и volume.

## Часть I. Docker

Сборка образа:

```sh
docker build -t lab-docker .
```

Запуск контейнера:

```sh
docker run -d --name lab_docker_app -p 5000:5000 lab-docker
```

Копирование README.md в каталог `/home/` контейнера:

```sh
docker cp README.md lab_docker_app:/home/README.md
```

Подключение к контейнеру в интерактивном режиме и проверка файла:

```sh
docker exec -it lab_docker_app sh
ls -la /home
exit
```

Остановка контейнера:

```sh
docker stop lab_docker_app
docker rm lab_docker_app
```

## Часть II. Docker Compose

Запуск приложения и базы данных:

```sh
docker compose up --build
```

После запуска приложение доступно в браузере по адресу:

```text
http://localhost:5000
```

Проверка работы приложения:

1. Открыть `http://localhost:5000`.
2. Ввести название задачи.
3. Нажать кнопку добавления.
4. Убедиться, что задача появилась в списке.

## Вывод

Домашнее задание выполнено: приложение запускается в Docker-контейнере, а через Docker Compose поднимается связка web-приложения и базы данных MySQL.

## Ссылка

https://github.com/NorthDakota11/lab8
