from django.urls import path
from .views import UserRegister, UserViewSet
from rest_framework.authtoken import views as auth_token
from rest_framework import routers

app_name = 'account'

urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('api-token-auth/', auth_token.obtain_auth_token),
]

router = routers.SimpleRouter()
router.register('user', viewset=UserViewSet, basename='list')
urlpatterns += router.urls
