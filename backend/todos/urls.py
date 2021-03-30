# todos/urls.py

from django.urls import path
from .views import ListTodo, DetailTodo


urlpatterns = [
    path('<int:pk>/', DetailTodo.as_a_view()),
    path('', ListTodo.as_a_view()),
]
