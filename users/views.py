from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect

from .models import User


class UserLoginView(LoginView):
    template_name = 'LR/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')


class UserLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
