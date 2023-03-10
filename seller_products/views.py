from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class SellerProductViewSet(ModelViewSet):
    serializer_class = serializers.SellerProductSerializer
    queryset = models.SellerProduct.objects.filter(is_active=True)
