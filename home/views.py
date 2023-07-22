from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Car


# Create your views here.

class Home(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context
