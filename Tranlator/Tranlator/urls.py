from django.contrib import (
    admin,
)  # Импортируем модуль для административной панели Django.
from django.urls import (
    path,
    include,
)  # Импортируем функции для работы с маршрутами URL Django.
from django.contrib.auth import (
    views as auth_views,
)  # Импортируем представления авторизации Django.
from main.views import (
    SignupView,
)  # Импортируем пользовательское представление для регистрации.

# Определяем переменную urlpatterns, которая содержит список маршрутов URL.
urlpatterns = [
    path("admin/", admin.site.urls),  # Маршрут для административной панели
    path("", include("main.urls")),  # Включаем маршруты из приложения main
    path(
        "signup/", SignupView.as_view(), name="signup"
    ),  # Маршрут для регистрации нового пользователя.
    path(
        "login/", auth_views.LoginView.as_view(), name="login"
    ),  # Маршрут для входа пользователя.
    # Маршрут для входа пользователя
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
]
