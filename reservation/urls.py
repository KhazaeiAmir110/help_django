from django.conf.urls import include
from django.urls import path
# from .views import ReservationViewSet
from rest_framework import routers
from test_reserv.views import ReservationViewSet

router = routers.SimpleRouter()
# router.register(r'list', ReservationViewSet)
router.register(r'create', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
