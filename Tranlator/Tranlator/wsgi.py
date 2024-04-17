# Импортируем модуль os для работы с операционной системой.
import os

# Импортируем функцию get_wsgi_application
# для получения WSGI-совместимого приложения Django.
from django.core.wsgi import (
    get_wsgi_application,
)

# Устанавливаем значение переменной
# окружения DJANGO_SETTINGS_MODULE, чтобы
# Django знал, какие настройки использовать.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tranlator.settings")

# Получаем WSGI-совместимое приложение Django,
# которое будет обрабатывать веб-запросы.
application = get_wsgi_application()
