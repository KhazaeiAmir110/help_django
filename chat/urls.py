from django.urls import path
from .views import RegisterAPIView, EmailVerificationAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('verify-email/', EmailVerificationAPIView.as_view(), name='verify-email'),
]
