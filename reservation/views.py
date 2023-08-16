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


class ReservationViewSet(mixins.CreateModelMixin,
                         GenericViewSet):
    queryset = Reservation.objects.filter()
    serializer_class = ReservationCreateOutputSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
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
        return Response(reservation_serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class ReservationListViewSet(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             GenericViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationListSerializer
    lookup_field = 'id'
    filter_backends = [
        filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter
    ]
    search_fields = ['user_name', ]
    filterset_fields = ['user', ]
    ordering_fields = 'created'

    class CustomPagination(PageNumberPagination):
        page_size = 10
        page_size_query_param = 'page_size'
        max_page_size = 100

    pagination_class = CustomPagination


class UserReservationListAPIView(generics.ListAPIView):
    serializer_class = ReservationListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Reservation.objects.filter(user=user)
