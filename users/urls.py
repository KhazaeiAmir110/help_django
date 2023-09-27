from django.urls import path, include
from .views import (ProfileView, CreateDemandView, EditProfileView,
                    ProfileHomeView, DemandCreate, DemandUpdateView,
                    DemandDeleteView)

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('create/', CreateDemandView.as_view(), name='create'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
    #     ____________________________________________________________________
    path('home/', ProfileHomeView.as_view(), name='home-profile'),
    path('demand/create/', DemandCreate.as_view(), name='demand-create'),
    path('demand/update/<int:pk>/', DemandUpdateView.as_view(), name='demand-update'),
    path('demand/delete/<int:pk>/', DemandDeleteView.as_view(), name='demand-delete'),
]
