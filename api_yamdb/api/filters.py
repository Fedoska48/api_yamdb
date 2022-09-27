from django_filters.rest_framework import (AllValuesFilter, CharFilter,
                                           FilterSet, NumberFilter)
from titles.models import Title


class TitleFilter(FilterSet):
    """Фильтр по полям произведений."""
    name = CharFilter(field_name='name', lookup_expr='icontains')
    year = NumberFilter(field_name='year')
    category = AllValuesFilter(field_name='category__slug',
                               lookup_expr='icontains')
    genre = AllValuesFilter(field_name="genre__slug",
                            lookup_expr='icontains')

    class Meta:
        model = Title
        fields = ('name', 'year', 'category', 'genre')
