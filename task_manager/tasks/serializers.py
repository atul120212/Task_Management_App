from rest_framework import serializers
from .models import Task
from users.models import User


class AssignedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']


class TaskWithoutAssignedUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # Exclude assigned_users from the response
        exclude = ['assigned_users']
        
class TaskSerializer(serializers.ModelSerializer):
    assigned_users = AssignedUserSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['created_at']
    def validate(self, data):
        # Ensure that assigned_users is optional
        if 'assigned_users' not in data:
            data['assigned_users'] = []
        return data
