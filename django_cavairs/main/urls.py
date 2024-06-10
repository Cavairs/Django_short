from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('times', views.times, name='times'),  # Время
    path('direct', views.direct, name='direct'),  # Директория
]
