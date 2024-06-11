from django.urls import path

from .views import ProfileUserView

urlpatterns = [
    path('', ProfileUserView.as_view(), name='profileuser'),
]
