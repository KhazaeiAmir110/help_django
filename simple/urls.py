from django.urls import path, include
from rest_framework import routers
from simple.views import PostViewSet, UserViewSet, PostImageViewSet, PostVideoSerializer

app_name = 'simple'

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename="users")
router.register('post', PostViewSet, basename='post-view')
router.register('post-image', PostImageViewSet, basename='post-image-view')
router.register('post-video', PostVideoSerializer, basename='post-video-view')

urlpatterns = [
    path('', include(router.urls))
]
