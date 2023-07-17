from django.urls import path
from .views import UserRegister, UserViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'account'

urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = routers.SimpleRouter()
router.register('user', viewset=UserViewSet, basename='list')
urlpatterns += router.urls
