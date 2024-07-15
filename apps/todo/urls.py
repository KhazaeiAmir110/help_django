from django.urls import path

from .views import lists, list_detail

urlpatterns = [
    path('', lists, name='todo-list'),
    path('<int:id>/', list_detail, name='detail'),
]
