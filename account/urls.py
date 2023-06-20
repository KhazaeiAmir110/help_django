from django.urls import path
from .views import UserRegister
from rest_framework.authtoken import views as auth_token

app_name = 'account'

urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('api-token-auth/', auth_token.obtain_auth_token),
]
