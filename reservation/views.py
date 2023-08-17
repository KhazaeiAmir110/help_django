from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status, filters, generics
from .models import Reservation
from .serializers import (
    ReservationCreateOutputSerializer, ReservationListSerializer, ReservationCreateInputSerializer
)
from rest_framework.permissions import IsAuthenticated
from user.models import User
from documentation.models import Documentation


class ReservationViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         GenericViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationCreateOutputSerializer
    lookup_field = 'id'
    filter_backends = [
        filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter
    ]
    permission_classes = (IsAuthenticated,)
    search_fields = ['user_name', ]
    filterset_fields = ['user', ]
    ordering_fields = 'created'

    class CustomPagination(PageNumberPagination):
        page_size = 10
        page_size_query_param = 'page_size'
        max_page_size = 100

    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'list':
            return queryset.filter(user=self.request.user)

        return queryset

    def create(self, request, *args, **kwargs):
        documentation = Documentation.objects.get(id=request.POST.get('documentation'))
        if (request.user.status == 'N' and str(
                documentation.status) == 'A') or request.user.status == 'S':
            from test_reserv.tasks import add_payment
            add_payment()
            serializer = ReservationCreateInputSerializer(
                data=dict(
                    user=request.user.id,
                    documentation=request.data.get('documentation')
                )
            )
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            reservation_serializer = ReservationCreateOutputSerializer(serializer.instance)

            headers = self.get_success_headers(reservation_serializer.data)
            documentation.status = 'U'
            return Response(reservation_serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        from test_reserv.tasks import add_payment
        add_payment()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ReservationListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ReservationListSerializer(queryset, many=True)
        return Response(serializer.data)
