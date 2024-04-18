import os  # Импортируем модуль os для работы с операционной системой.
from pathlib import (
    Path,
)

# Импортируем Path из pathlib для работы с путями к файлам и директориям.
# для работы с путями к файлам и директориям.


# Определяем базовый каталог проекта.
BASE_DIR = Path(__file__).resolve().parent.parent

# Определяем каталог, в котором будут храниться шаблоны (HTML-файлы) проекта.
TEMPLATES_DIR = os.path.join(BASE_DIR, "main", "templates")

SECRET_KEY = "django-insecure-9k_5j(^s_ap9%8ep9^y1ihi10cw-*m59kq3&=4bo_7nps"
# Секретный ключ Django.

DEBUG = True
# Режим отладки, который выводит ошибки для разработки,
# но должен быть отключен в продакшене

ALLOWED_HOSTS = []  # Список хостов, которые могут обслуживать ваше приложение.
# Пустой список разрешает все хосты.

INSTALLED_APPS = [  # Список установленных приложений Django.
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
]
# Список промежуточных слоев (middleware) обрабатывают запросы и ответы.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Tranlator.urls"  # Корневой URL-конфигурации проекта.

TEMPLATES = [  # Конфигурация шаблонов Django.
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        # Директории, в которых Django будет искать шаблоны.
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = (
    "Tranlator.wsgi.application"
    # WSGI-приложение для развертывания на веб-сервере.
)

DATABASES = {  # Настройки базы данных.
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        # Используем SQLite в качестве базы данных по умолчанию.
        "NAME": BASE_DIR / "db.sqlite3",  # Путь к файлу базы данных SQLite.
    }
}

# Настройки валидации пароля пользователей Django.
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"  # Язык по умолчанию.

TIME_ZONE = "UTC"  # Часовой пояс по умолчанию.

USE_I18N = True  # Включение международной локализации.

USE_TZ = True  # Использование временных зон.

STATIC_URL = "static/"  # URL для статических файлов.

# Директории, в которых Django будет искать статические файлы.
STATICFILES_DIRS = [
    "D:/CodingPractic/Full-stack/Tranlator/main/static",
    os.path.join(BASE_DIR, "static"),
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# Настройка для поля автоматического увеличения в моделях Django.
