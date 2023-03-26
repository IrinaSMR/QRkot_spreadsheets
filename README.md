# Приложение для Благотворительного фонда поддержки котиков QRkot_spreadseets

## Описание

Проект написан на фреймворке FastAPI с возможностью формирования отчетов в Google Sheets с использованием хранилища Google Drive.

**QRkot** - это API сервиса по сбору средств для финансирования благотворительных проектов. В сервисе реализована возможность регистрации пользователей, добавления благотворительных проектов и пожертвований, которые распределяются по открытым проектам.

Настроено автоматическое создание первого суперпользователя при запуске проекта.

Реализована возможность получения отчета с перечнем проектов с закрытыми сборами, отсортированных по времени закрытия.

## Ключевые технологии и библиотеки:
- Python
- FastAPI
- SQLAlchemy
- Alembic
- Pydantic

## Установка
1. Склонируйте репозиторий:
```
https://github.com/IrinaSMR/QRkot_spreadsheets.git
```
2. Активируйте venv и установите зависимости:
```
python -m venv venv
source venv/Scripts/activate
python -m pip install upgrade pip
pip install -r requirements.txt
```
3. Создайте в корневой директории файл .env со следующим наполнением:
```
APP_TITLE=QRkot
APP_DESCRIPTION=Сервис поддержки котиков
DATABASE_URL='sqlite+aiosqlite:///./fastapi.db'
SECRET=<secret>
FIRST_SUPERUSER_EMAIL=<email superuser>
FIRST_SUPERUSER_PASSWORD=<password superuser>
TYPE=service_account
PROJECT_ID=atomic-climate-<идентификатор>
PRIVATE_KEY_ID=<id приватного ключа>
PRIVATE_KEY="-----BEGIN PRIVATE KEY-----<приватный ключ>-----END PRIVATE KEY-----\n"
CLIENT_EMAIL=<email сервисного аккаунта>
CLIENT_ID=<id сервисного аккаунта>
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=<ссылка>
EMAIL=<email пользователя>

```
4. Примените миграции для создания базы данных SQLite, если потребуется:
```
alembic init --template async alembic
alembic revision --autogenerate -m "Name of Migration"
alembic upgrade head
```
5. Проект готов к запуску.

Для локального запуска выполните команду:
```
uvicorn app.main:app --reload
```
Сервис запущен и доступен по следующим адресам:
- http://127.0.0.1:8000/redoc
- http://127.0.0.1:8000/docs

### Автор
IrinaSMR
