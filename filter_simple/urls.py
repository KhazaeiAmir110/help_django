from django.urls import path, include
from rest_framework import routers
from filter_simple.views import PostViewSet, PostImageViewSet, HumanViewSet

app_name = 'filter_simple'

router = routers.SimpleRouter()
router.register('post-filter', PostViewSet, basename='post-view-filter')
router.register('post-image-filter', PostImageViewSet, basename='post-image-view-filter')
router.register('human', HumanViewSet, basename='filter-human')

urlpatterns = [
    path('', include(router.urls))
]
