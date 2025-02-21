from django.urls import path

from cache.views import view_one, set_session, get_session

urlpatterns = [
    path('test/', view_one),
    path('s/', set_session),
    path('g/', get_session),
]
