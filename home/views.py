from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from .models import Car


# Create your views here.

class Home(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context


class Two(RedirectView):
    # # برای انتقال به سایت های دیگر
    # url = 'https://www.django-rest-framework.org/api-guide/pagination/'

    # برای انتقال به خود صفحه های سایت
    pattern_name = 'home:home'

    # # برای کارهای seo البته کار همون pattern_name زو انجام میده
    # permanent = 'home:home'

    # اگر مقدار دهی اضافی به url بدهیم هیچ ارروری رخ نمیدهد
    query_string = True

    # نمایش در terminal
    def get_redirect_url(self, *args, **kwargs):
        print('*' * 90)
        print('print')
        return super().get_redirect_url(*args, **kwargs)
