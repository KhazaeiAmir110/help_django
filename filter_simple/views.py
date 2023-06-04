from rest_framework.viewsets import ModelViewSet
from filter_simple.serializer import PostSerializer, PostImageSerializer
from filter_simple.models import Post, PostImage


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ["category"]


class PostImageViewSet(ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    filterset_fields = ["post"]
