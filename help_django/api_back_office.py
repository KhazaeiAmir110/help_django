from django.conf.urls import include
from django.urls import path

from user.urls import backoffice_router

urlpatterns = [
    path('back_office/', include(backoffice_router.urls)),
]
