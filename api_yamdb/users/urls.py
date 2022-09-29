from api.views import UserViewSet, create_token, create_user
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'v1/users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/auth/signup/', create_user),
    path('v1/auth/token/', create_token),
]
