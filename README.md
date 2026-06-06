# lab08

Лабораторная работа по Docker выполнена по заданию из репозитория `tp-lessons/lab_docker`.

## Суть задания

Нужно подготовить web-приложение в каталоге `app/`, добавить Dockerfile, настроить запуск приложения в контейнере и создать `docker-compose.yml` для совместной работы приложения и базы данных MySQL.

## Состав проекта

- `app/main.py` — Flask-приложение для добавления задач.
- `requirements.txt` — зависимости Python.
- `db/init.sql` — SQL-файл инициализации таблицы задач.
- `Dockerfile` — сборка Docker-образа web-приложения.
- `docker-compose.yml` — запуск приложения и MySQL.
- `REPORT.md` — отчет по домашнему заданию.

## Команды проверки

```sh
docker build -t lab-docker .
docker run --rm -it -p 5000:5000 lab-docker
```

Для запуска связки приложение + база данных:

```sh
docker compose up --build
```

После запуска приложение доступно по адресу `http://localhost:5000`.

## Ссылка

https://github.com/NorthDakota11/lab8
