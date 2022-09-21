from django.urls import include, path
from rest_framework import routers

from reviews.views import CommentViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register('reviews', ReviewViewSet, basename='reviews')
# router.register('groups', GroupViewSet, basename='groups')
router.register(r'reviews/(?P<review_id>\d+)/comments', CommentViewSet,
                basename='comments')
# router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
