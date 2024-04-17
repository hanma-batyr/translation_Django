from django.apps import AppConfig


# Класс MainConfig определяет конфигурацию приложения "main".
class MainConfig(AppConfig):
    # Настройка для поля автоматического увеличения в моделях Django.
    default_auto_field = "django.db.models.BigAutoField"

    # Имя приложения.
    name = "main"
