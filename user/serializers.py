from rest_framework import serializers
from .models import User


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'name', 'age', 'image', 'email', 'is_active',
            'is_staff', 'status'
        )


class UserBackOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'phone_number', 'name', 'age', 'image', 'email', 'is_active',
            'is_staff', 'status',
        )
