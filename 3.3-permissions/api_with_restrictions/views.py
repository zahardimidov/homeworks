from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from .filters import AdvertisementFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from advertisements.permissions import IsOwnerOrReadOnly
from rest_framework.pagination import LimitOffsetPagination

from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AdvertisementFilter

    filterset_fields = ['user']
    ordering_fields = ['created_at', 'status']
    pagination_class = LimitOffsetPagination

    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action != 'GET':
    #         return [IsAuthenticated()]
    #     return []

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

