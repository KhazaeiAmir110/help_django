from django.conf.urls import include
from django.urls import path
from .views import (
    ReservationViewSet, ReservationListViewSet, UserReservationListAPIView,
)
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'create', ReservationViewSet)
router.register(r'list', ReservationListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list-user-reservation/', UserReservationListAPIView.as_view())
]
