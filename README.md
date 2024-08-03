# MessageApp

## Описание

Этот проект включает в себя FastAPI веб-приложение,
Telegram-бота, MongoDB для хранения данных,
Nginx в качестве веб-сервера
и Redis для кэширования.

## Структура проекта

```plaintext
MsgService/
│
├── chat_bot/
│   ├── handlers/
│   │   ├── __init__.py
│   │   └── client.py 
│   ├── bot_initializer.py
│   ├── bot_run.py
│   ├── Dockerfile
│   ├── .env
│   └── requirements.txt
│
├── web/
│   ├──__init__.py
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── nginx/
│   ├── conf.d
│   │   └──default.conf
│   ├── nginx.conf
│   └── Dockerfile
│
├── docker-compose.yml
├── .gitingnore
├── .dockeringnore
│
└── README.md
```
## Установка и запуск

1. Клонируйте репозиторий:
    ```sh
    git clone <LINK>
    cd project
    ```

2. Создайте файл `.env` в папке chat_bot и добавьте в него переменные окружения:
    ```sh
    TELEGRAM_TOKEN=your_telegram_bot_token
    ```

3. Запустите Docker Compose:
    ```sh
    docker-compose up --build
    ```
    В новой веррсии Docker:
    ```sh
    docker compose up --build
    ```

## API Endpoints

- `GET /api/v1/messages/` - Получить список всех сообщений.
- `POST /api/v1/message/` - Создать новое сообщение.

## Использование Telegram бота

- `/start` - Приветственное сообщение.
- `/new <your_message>` - Создать новое сообщение.
- `/messages` - Показать все сообщения.


## Кэширование

Список сообщений кэшируется с помощью Redis.

