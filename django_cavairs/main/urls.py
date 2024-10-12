from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    # path('sort', views.sort, name='sort'),  # Omlet
    # path('omlet/<int:servings>/', views.omlet, name='servings'),
    # path('pasta', views.pasta, name='pasta'),  # Pasta
    # path('buter', views.pasta, name='buter'),  # buter
]
