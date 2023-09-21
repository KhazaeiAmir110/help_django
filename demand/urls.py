from django.urls import path
from .views import Home, Post, Category, EditPostView

app_name = 'demand'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<slug:slug>/', Post.as_view(), name='post'),
    path('category/<slug:slug>/', Category.as_view(), name='category'),
    path('edit_profile/<slug:slug>/', EditPostView.as_view(), name='edit-post'),
]
