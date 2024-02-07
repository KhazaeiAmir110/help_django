from django.shortcuts import render, redirect
import random
from django.contrib import messages

from django.views import View
from .forms import UserRegisterForm, VerifyCodeForm
from cor.utils import send_otp_code
from .models import OtpCode, User


class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(10000, 99999)
            send_otp_code(form.changed_data[2], code=random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
            request.session['user_register_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'we sent you a code', 'success')
            return redirect('accounts:verify_code')
        return redirect(request, self.template_name, {'form': form})


class UserRegisterVerifyCode(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_register_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if code_instance.code == cd['code']:
                User.object.create_user(user_session['phone_number'],
                                        user_session['email'],
                                        user_session['full_name'],
                                        user_session['password'])
                code_instance.delete()
                messages.success(request, 'you registered.', 'success')
                return redirect('home:home')
            else:
                messages.error(request, 'This is code wrong!!!', 'danger')
                return redirect('accounts:verify_code')
        return redirect('home:home')
