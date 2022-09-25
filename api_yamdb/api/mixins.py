from rest_framework.viewsets import GenericViewSet

from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin
)


class GetListCreateDeleteMixin(GenericViewSet, CreateModelMixin,
                               ListModelMixin, DestroyModelMixin):
    pass
