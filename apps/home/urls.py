from django.urls import path
from .views import HomeView, AboutView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/<str:username>/', AboutView.as_view(), name='about'),
]
