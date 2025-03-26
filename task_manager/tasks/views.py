from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from .models import Task
from .serializers import TaskSerializer, TaskWithoutAssignedUsersSerializer
from rest_framework import generics


class UserTasksView(APIView):
    def get(self, user_id):
        tasks = Task.objects.filter(assigned_users__id=user_id)  # Filter tasks for the specific user
        serializer = TaskWithoutAssignedUsersSerializer(tasks, many=True)
        return Response(serializer.data)
        
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.prefetch_related('assigned_users')  # Prefetch assigned users for optimization
    serializer_class = TaskSerializer

class TasksForUserView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Task.objects.filter(assigned_users__id=user_id)
    
class AssignTaskView(APIView):
    def post(self, request, task_id):
        try:
            # Fetch the task to which users will be assigned
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        # Extract email IDs from the request data
        email_ids = request.data.get('emails', [])
        if not email_ids:
            return Response({'error': 'No email IDs provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch users based on email IDs
        users = User.objects.filter(email__in=email_ids)
        if not users.exists():
            return Response({'error': 'No valid users found for the provided email IDs'}, status=status.HTTP_400_BAD_REQUEST)

        # Assign users to the task
        task.assigned_users.set(users)  # Overwrites previous assignments
        task.save()

        # Serialize and return the updated task
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)