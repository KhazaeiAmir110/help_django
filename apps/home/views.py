from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserRegistrationForm


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class AboutView(View):
    def get(self, request, username):
        return render(request, 'home.html')


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super.dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            messages.success(request, 'your registered successfully', 'success')
            return redirect('home:home')
        return render(request, self.template_name, {'form': form})
