from rest_framework import serializers
from django.contrib.auth.models import User

from account.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("id", "username", "password", 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'message': 'Password fields does not match'}
            )
        return data

    def create(self, data):
        user = User.objects.create(
            username=data['username'],
        )
        user.set_password(data['password'])
        user.save()
        UserProfile.objects.create(user=user)
        return user
