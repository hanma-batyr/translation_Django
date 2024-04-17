import os  # Импортируем модуль os для работы с операционной системой.

from django.core.asgi import (
    get_asgi_application,
)  # Импортируем функцию get_asgi_application

# для получения ASGI-совместимого приложения Django.

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "Translator.settings"
)  # Устанавливаем значение переменной
# окружения DJANGO_SETTINGS_MODULE, чтобы
# Django знал, какие настройки использовать.

application = get_asgi_application()
# Получаем ASGI-совместимое приложение Django,
# которое будет обрабатывать веб-запросы.
