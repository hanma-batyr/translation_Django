from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignupView.as_view(), name='signup'),  # Используйте ваш SignupView
    path('login/', views.login, name='login'),
]