from django.db import models
from users.models import User

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=50, choices=[('personal', 'Personal'), ('work', 'Work')])
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    assigned_users = models.ManyToManyField('users.User', related_name='assigned_tasks', blank=True )
    # creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')

    def __str__(self):
        return self.name
