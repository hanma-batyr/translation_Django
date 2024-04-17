# Импорт необходимых модулей и классов Django для работы с представлениями.
from django.shortcuts import render, redirect
from googletrans import Translator, LANGUAGES
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import TranslationHistory
from django.contrib.auth import logout


# Класс представления для регистрации новых пользователей.
class SignupView(CreateView):
    form_class = UserCreationForm  # Используем встроенную форму UserCreationForm для регистрации.
    success_url = reverse_lazy(
        "index"
    )  # После успешной регистрации перенаправляем на главную страницу.
    template_name = "registration/signup.html"  # Используем шаблон для регистрации.

    # Переопределяем метод form_valid для выполнения дополнительных действий после успешного сохранения формы.
    def form_valid(self, form):
        user = form.save()  # Сохраняем данные нового пользователя.
        auth_login(self.request, user)  # Выполняем вход для нового пользователя.
        return super().form_valid(
            form
        )  # Вызываем метод form_valid родительского класса.


# Функция представления для регистрации новых пользователей.
def signup(request):
    # Если метод запроса POST, обрабатываем форму регистрации.
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем данные нового пользователя.
            auth_login(request, user)  # Выполняем вход для нового пользователя.
            return redirect(
                "index"
            )  # Перенаправляем на главную страницу после успешной регистрации.
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


# Функция представления для входа пользователей.
def login_user(request):
    # Если метод запроса POST, обрабатываем форму входа.
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(
                username=username, password=password
            )  # Аутентифицируем пользователя.
            if user is not None:
                auth_login(request, user)  # Выполняем вход пользователя.
                return redirect("index")  # Перенаправляем на главную страницу.
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})


# Функция представления для главной страницы перевода текста.
def index(request):
    # Если метод запроса POST, обрабатываем перевод текста.
    if request.method == "POST":
        source_lang = request.POST.get("source_lang")
        target_lang = request.POST.get("target_lang")
        txt = request.POST.get("input_text")

        # Создаем экземпляр класса Translator для выполнения перевода.
        translator = Translator()

        # Определяем язык текста автоматически.
        detected_lang = translator.detect(txt).lang

        # Если язык текста не определен, используем исходный язык.
        if detected_lang == "unknown":
            detected_lang = source_lang

        # Переводим текст на целевой язык.
        translation = translator.translate(txt, src=detected_lang, dest=target_lang)

        # Получаем переведенный текст.
        translated_text = translation.text

        # Сохраняем историю перевода, если пользователь аутентифицирован.
        if request.user.is_authenticated:
            TranslationHistory.objects.create(
                user=request.user,
                source_text=txt,
                source_lang=detected_lang,
                target_text=translated_text,
                target_lang=target_lang,
            )

        return JsonResponse(
            {"result": translated_text}
        )  # Возвращаем результат перевода в формате JSON.

    # Если это не POST-запрос, просто возвращаем страницу с формой перевода.
    return render(request, "main/main.html", {"languages": LANGUAGES.items()})


# Функция представления для просмотра истории переводов пользователя.
@login_required(
    login_url="/login/"
)  # Декоратор, требующий аутентификации пользователя.
def translation_history(request):
    history = TranslationHistory.objects.filter(
        user=request.user
    )  # Получаем историю переводов текущего пользователя.
    return render(
        request, "history/history.html", {"history": history}
    )  # Отображаем историю переводов.


# Функция представления для просмотра профиля пользователя.
@login_required(
    login_url="/login/"
)  # Декоратор, требующий аутентификации пользователя.
def profile(request):
    user = request.user  # Получаем текущего пользователя.
    return render(
        request, "profile/profile.html", {"user": user}
    )  # Отображаем профиль пользователя.


# Функция для выхода пользователя из системы.
def logout_view(request):
    logout(request)  # Выполняем выход пользователя из системы.
    return redirect("index")  # Перенаправляем на главную страницу.
