from django.urls import path

from first_celery.views import firstCelery

urlpatterns = [
    path('', firstCelery),
]
