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
    model = Car  # object_list
    # یا باید در html cars را عوض کنیم و object_list بنویسیم یا متد زیر رو بنویسیم
    context_object_name = 'cars'

    # ترتیب
    ordering = 'year'
