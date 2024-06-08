from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.views import View

from .models import User
from .forms import RegistrationForm


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


class UserRegisterView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            template_name = 'LR/register.html'
            return render(request, template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')

        form_class = RegistrationForm(request.POST)

        if form_class.is_valid():
            if (User.objects.filter(email=email).exists() or
                    User.objects.filter(username=username).exists() or
                    password != password2):
                return redirect('register')

            User.objects.create_user(username=username, email=email, password=password)
            return redirect('home')
        else:
            template_name = 'LR/register.html'
            return render(request, template_name)
