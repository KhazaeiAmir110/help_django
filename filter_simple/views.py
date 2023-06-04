from rest_framework.viewsets import ModelViewSet
from filter_simple.serializer import PostSerializer, PostImageSerializer
from filter_simple.models import Post, PostImage
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]


class PostImageViewSet(ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["post"]


class HumanViewSet(ModelViewSet):
    queryset = Post.objects.filter(category=2)
    serializer_class = PostSerializer
