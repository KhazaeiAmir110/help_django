from django.urls import path

from first_celery.views import home

urlpatterns = [
    path('', home),
]
