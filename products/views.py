from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from . import models, serializers, permissions
from utils import mixins


class ProductImageViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    serializer_class = serializers.ProductImageSerializer
    queryset = models.ProductImage.objects.all()


class ProductViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    ACTION_SERIALIZERS = {
        'retrieve': serializers.RetrieveProductSerializer,
    }
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()

    permission_classes = (permissions.IsMe,)

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return IsAuthenticated(),

        return permissions.IsMe(),

    def list(self, request, *args, **kwargs):
        print(type(request.user))

        return super().list(request, *args, **kwargs)
