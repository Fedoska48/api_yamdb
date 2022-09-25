from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend

from .permissions import IsAdminOrReadOnly
from rest_framework import viewsets

from .serializers import (TitleSerializer, CategorySerializer,
                                           GenreSerializer)
from titles.models import Title, Category, Genre


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [IsAdminOrReadOnly, ]

    def get_queryset(self):
        queryset = Title.objects.all().annotate(
            Avg("reviews__score")).order_by("name")
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly, ]


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly, ]