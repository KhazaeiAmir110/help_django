from rest_framework import serializers
from simple.models import Post
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('created', 'updated')
