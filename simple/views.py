from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from simple.serializer import PostSerializer, UserSerializer, PostImageSerializer, \
    PostVideoSerializer
from simple.models import Post, PostImage, PostVideo


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostImageViewSet(ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer


class PostVideoSerializer(ModelViewSet):
    queryset = PostVideo.objects.all()
    serializer_class = PostVideoSerializer
