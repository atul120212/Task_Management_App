from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from django.urls import path
from .views import AssignTaskView,UserTasksView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('user/<int:user_id>/tasks', UserTasksView.as_view(), name='tasks_for_user'),
    path('tasks/<int:task_id>/assign/', AssignTaskView.as_view(), name='assign_task'),
]