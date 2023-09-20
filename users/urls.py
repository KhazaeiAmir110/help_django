from django.urls import path, include
from .views import ProfileView, CreateDemandView, EditProfileView

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('create/', CreateDemandView.as_view(), name='create'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
]
