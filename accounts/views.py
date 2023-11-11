from django.shortcuts import render, redirect
import random
from django.contrib import messages

from django.views import View
from .forms import UserRegisterForm, VerifyCodeForm
from cor.utils import send_top_code
from .models import OtpCode


class UserRegisterView(View):
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            # فرستادن کد و شماره تلفن به سرویس برای ارسال به کاربر
            send_top_code(form.changed_data['phone'], code=random_code)
            # save phone and code in database
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
            # save Information in session
            request.session['user_register_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'email ': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'we sent you a code', 'success')
            # if success sent code => new page
            return redirect('accounts:verify_code')
        return redirect('home:home')


class UserRegisterVerifyCode(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_register_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
