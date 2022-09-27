from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from reviews.models import Review
from titles.models import Category, Genre, Title

from .filters import TitleFilter
from .mixins import GetListCreateDeleteMixin
from .permissions import IsAdminModeratorAuthor, IsAdminOrReadOnly
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer, TitleSerializer,
                          TitleGetSerializer)


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для произведения."""
    queryset = Title.objects.all().annotate(
            Avg('reviews__score')).order_by('name').prefetch_related(
            'category', 'genre')
    serializer_class = TitleSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = TitleFilter
    permission_classes = [IsAdminOrReadOnly, ]

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH'):
            return TitleSerializer
        return TitleGetSerializer


class CategoryViewSet(GetListCreateDeleteMixin):
    """Вьюсет для категории."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly, ]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('name', 'slug')
    search_fields = ('name', 'slug',)
    lookup_field = 'slug'


class GenreViewSet(GetListCreateDeleteMixin):
    """Вьюсет для жанра."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('name', 'slug')
    search_fields = ('name', 'slug')
    lookup_field = 'slug'


class ReviewViewSet(viewsets.ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminModeratorAuthor, ]

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(title=title, author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAdminModeratorAuthor, ]

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)
