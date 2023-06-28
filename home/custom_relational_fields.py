from rest_framework import serializers


class UserEmailRelationalFields(serializers.RelatedField):
    def to_representation(self, value):
        return f'{value.username} - {value.email}'
