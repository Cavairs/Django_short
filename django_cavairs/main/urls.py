from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('omlet', views.omlet, name='omlet'),  # Omlet
    path('omlet/<int:servings>/', views.omlet, name='servings'),
    path('pasta', views.pasta, name='pasta'),  # Pasta
    path('buter', views.pasta, name='buter'),  # buter
]
