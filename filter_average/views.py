from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Category, Post
from .serializer import CategorySerializer, PostSerializer


class PostFilter(filters.FilterSet):
    category_name = filters.CharFilter(field_name='category__name', lookup_expr='iexact')

    class Meta:
        model = Post
        fields = ['category_name']


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PostFilter
