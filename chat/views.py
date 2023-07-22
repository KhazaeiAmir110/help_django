from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.utils.crypto import get_random_string

from .models import CustomUser, EmailVerificationToken
from .serializers import CustomUserSerializer, EmailVerificationTokenSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Create and save the email verification token
            user = serializer.instance
            token = get_random_string(length=64)
            email_token = EmailVerificationToken.objects.create(user=user, token=token)

            # Here, you can send an email with the verification token to the user's email address

            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class EmailVerificationAPIView(APIView):
    def post(self, request):
        token = request.data.get('token')
        try:
            email_token = EmailVerificationToken.objects.get(token=token)
            email_token.user.is_active = True
            email_token.user.save()
            email_token.delete()
            return Response({'message': 'Email verified successfully!'})
        except EmailVerificationToken.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=400)
