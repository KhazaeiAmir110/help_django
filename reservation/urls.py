from django.urls import path
from .views import HomeView, WorkDateView, WorkTimeView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:category_slug>/', HomeView.as_view(), name='category_filter'),
    path('work_time/<slug:company_slug>/', WorkDateView.as_view(), name='work_time'),
    path('work_time/<slug:company_slug>/<str:date>/', WorkTimeView.as_view(), name='work_hours')
]
