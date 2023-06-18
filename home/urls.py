from django.urls import path
from .views import Home

app_name = 'home'

urlpatterns = [
    path('<str:name>/', Home.as_view(), name='home')
]
