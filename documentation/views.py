from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, pagination, filters
from .models import Documentation
from .serializers import DocumentationSerializer
from django_filters.rest_framework import DjangoFilterBackend


class DocumentationViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer

    search_fields = ['name', ]
    filterset_fields = ['type', 'status', ]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter,
                       ]
    ordering_fields = ['name', 'author', ]

    class CustomPagination(pagination.PageNumberPagination):
        page_size = 3
        page_size_query_param = 'page_size'
        max_page_size = 100

    pagination_class = CustomPagination


class DocumentationBackOfficeViewSet(mixins.ListModelMixin,
                                     mixins.CreateModelMixin,
                                     mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin,
                                     GenericViewSet):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer
    lookup_field = 'id'
