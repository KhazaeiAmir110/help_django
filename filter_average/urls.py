from django.urls import path, include
from rest_framework import routers
from filter_average.views import PostList

app_name = 'filter_average'

router = routers.SimpleRouter()
router.register('post-filter', PostList, basename='post-view-filter')
# router.register('category', CategoryList, basename='post-image-view-filter')

urlpatterns = [
    path('', include(router.urls))
]
