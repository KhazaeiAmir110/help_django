from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<slug:my_slug>', views.CarDetail.as_view(), name='car_detail'),
]
