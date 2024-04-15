from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("translate/", views.index, name="translate"),  # Обрабатываем POST-запросы
    path(
        "signup/", views.SignupView.as_view(), name="signup"
    ),  # Используйте ваш SignupView
    path("login/", views.login, name="login"),
    path("history/", views.translation_history, name="history"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout_view, name="logout"),
]
