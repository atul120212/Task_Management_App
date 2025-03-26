from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from django.urls import path
from .views import RegisterUserView



router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('register/', RegisterUserView.as_view(), name='register_user')
]