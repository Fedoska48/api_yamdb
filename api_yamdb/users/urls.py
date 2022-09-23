from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, create_user, create_token

router = DefaultRouter()

router.register(r'v1/users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/auth/signup/', create_user),
    path('v1/auth/token/', create_token),
]
