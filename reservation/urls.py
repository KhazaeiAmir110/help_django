from django.conf.urls import include
from django.urls import path
from .views import ReservationViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'list', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
