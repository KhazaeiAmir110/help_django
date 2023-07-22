from django.urls import path
from .views import LoginAPIView, UserAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('user/', UserAPIView.as_view(), name='user'),
]
