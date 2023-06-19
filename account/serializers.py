from rest_framework import serializers
from django.contrib.auth.models import User


def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('admin cant be in email')
    elif '@gmail.com' is not value:
        raise serializers.ValidationError('email error')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('username cant be admin')
        return value
