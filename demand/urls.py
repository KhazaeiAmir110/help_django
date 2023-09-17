from django.urls import path
from .views import Home, Post, Form

app_name = 'demand'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<slug:slug>/', Post.as_view(), name='post'),
    path('form/', Form.as_view(), name='form'),
]
