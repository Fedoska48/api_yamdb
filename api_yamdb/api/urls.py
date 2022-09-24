from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CommentViewSet, ReviewViewSet, TitleViewSet, GenreViewSet,
                   CategoryViewSet)


app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('reviews', ReviewViewSet, basename='reviews')
# router.register('groups', GroupViewSet, basename='groups')
router_v1.register(r'reviews/(?P<review_id>\d+)/comments', CommentViewSet,
                basename='comments')
# router.register('follow', FollowViewSet, basename='follow')
router_v1.register(r'titles', TitleViewSet, basename='titles')
router_v1.register(r'genres', GenreViewSet, basename='genres')
router_v1.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
