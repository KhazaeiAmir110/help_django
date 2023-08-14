from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import Documentation
from .serializers import DocumentationSerializer


class DocumentationViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer


class DocumentationBackOfficeViewSet(mixins.ListModelMixin,
                                     mixins.CreateModelMixin,
                                     mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin,
                                     GenericViewSet):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer
    lookup_field = 'id'
