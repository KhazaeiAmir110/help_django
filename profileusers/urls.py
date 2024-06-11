from django.urls import path

from .views import HomeProfileView

urlpatterns = [
    path('', HomeProfileView.as_view(), name='home-profile'),
]
