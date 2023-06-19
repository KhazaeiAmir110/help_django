from django.urls import path
from .views import UserRegister

app_name = 'account'

urlpatterns = [
    path('register/', UserRegister.as_view())
]
