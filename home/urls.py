from django.urls import path

from .views import ListPostView, PostDetailView

urlpatterns = [
    path('', ListPostView.as_view(), name='home'),
    path('<str:title>/', PostDetailView.as_view(), name='post')
]
