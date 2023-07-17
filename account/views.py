from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class UserRegister(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, ]
    # فقط کسانی که ثبت نام کره اند میتوانند تغیرات را ایجاد کنند
    queryset = User.objects.all()

    def list(self, request):
        srz_data = UserSerializer(self.queryset, many=True)
        return Response(data=srz_data.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        # با توجه به متد get عمل retrive انجام میشود
        srz_data = UserSerializer(instance=user)
        return Response(data=srz_data.data)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        srz_data = UserSerializer(instance=user, data=request.POST, partial=True)
        # اگر اطلاعات فرستاده شده توسط کاربر دست بود
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data)
        return Response(data=srz_data.errors)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        user.is_active = False  # غیر فعال کردن آن کاربر
        user.save()
        return Response({'massage': 'user deactivated'})
