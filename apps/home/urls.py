from django.urls import path
from .views import HomeView, AboutView, UserRegisterView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/<str:username>/', AboutView.as_view(), name='about'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
]
