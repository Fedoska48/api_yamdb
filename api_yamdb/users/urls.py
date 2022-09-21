from django.urls import path

from .views import create_user, create_token

urlpatterns = [
    path('auth/signup/', create_user),
    path('auth/token/', create_token),
]
