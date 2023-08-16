from rest_framework import serializers
from .models import Reservation


class ReservationListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    documentation_name = serializers.CharField(source='documentation.name', read_only=True)

    class Meta:
        model = Reservation
        fields = (
            'id', 'user_name', 'documentation_name', 'created')


class ReservationCreateOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'id', 'user', 'documentation', 'created', 'updated'
        )


class ReservationCreateInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('documentation', 'user')
