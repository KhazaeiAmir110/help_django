from django.conf.urls import include
from django.urls import path
from .views import UserViewSet, UserBackOfficeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

backoffice_router = routers.SimpleRouter()
backoffice_router.register(r'', UserBackOfficeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
