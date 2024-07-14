from django.urls import path

from .views import list_detail

urlpatterns = [
    path('', list_detail, name='todo-list')
]
