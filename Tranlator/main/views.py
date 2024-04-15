# main/views.py
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


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("index")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return super().form_valid(form)


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})


def index(request):
    if request.method == "POST":
        source_lang = request.POST.get("source_lang")
        target_lang = request.POST.get("target_lang")
        txt = request.POST.get("input_text")

        # Создаем экземпляр класса Translator
        translator = Translator()

        # Определяем язык текста автоматически
        detected_lang = translator.detect(txt).lang

        # Если язык текста не определен, используем исходный язык
        if detected_lang == "unknown":
            detected_lang = source_lang

        # Переводим текст на целевой язык
        translation = translator.translate(txt, src=detected_lang, dest=target_lang)

        # Получаем переведенный текст
        translated_text = translation.text

        # Сохраняем историю перевода
        if request.user.is_authenticated:  # Проверяем, аутентифицирован ли пользователь
            TranslationHistory.objects.create(
                user=request.user,
                source_text=txt,
                source_lang=detected_lang,
                target_text=translated_text,
                target_lang=target_lang,
            )

        return JsonResponse({"result": translated_text})

    # Если это не POST-запрос, просто возвращаем страницу
    return render(request, "main/main.html", {"languages": LANGUAGES.items()})


@login_required
def translation_history(request):
    history = TranslationHistory.objects.filter(user=request.user)
    return render(request, "history/history.html", {"history": history})


@login_required
def profile(request):
    user = request.user
    return render(request, "profile/profile.html", {"user": user})


def logout_view(request):
    logout(request)
    return redirect(
        "index"
    )  # Замените 'index' на имя вашего представления главной страницы
