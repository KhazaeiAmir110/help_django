from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from simple.serializer import PostSerializer


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PostSerializer
