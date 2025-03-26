from rest_framework import serializers
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'mobile', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get('username', ''),
            name=validated_data['name'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password']
        )
        return user
