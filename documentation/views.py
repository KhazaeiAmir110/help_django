import json
import redis_app.services as redis_services

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, pagination, filters
from rest_framework.response import Response
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

    def list(self, request, *args, **kwargs):
        documentation_list = redis_services.get('documentation_list')
        if documentation_list:
            return Response(json.loads(documentation_list))

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        redis_services.set('documentation_list', json.dumps(serializer.data))
        return Response(serializer.data)
