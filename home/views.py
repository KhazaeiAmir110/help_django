from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from .models import Car
from django.views.generic.list import ListView


# Create your views here.
#
# class Home(TemplateView):
#     template_name = 'home/home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cars'] = Car.objects.all()
#         return context

class Home(ListView):
    template_name = 'home/home.html'
    queryset = Car.objects.filter(year__gte=2000)
    context_object_name = 'cars'

    # برای اعمال بیشتر باید در تابع بنویسیم
    def get_queryset(self):
        result = Car.objects.filter(year__gte=2000)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = 'jack'
        return context
