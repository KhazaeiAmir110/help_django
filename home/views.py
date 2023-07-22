from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from .models import Car
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class Home(ListView):
    template_name = 'home/home.html'
    model = Car
    context_object_name = 'cars'


class CarDetail(DetailView):
    template_name = 'home/detail.html'

    def get_object(self, queryset=None):
        return Car.objects.get(
            # kwargs : دسترسی به پاراماتر های دیگر
            name=self.kwargs['name'],
            owner=self.kwargs['owner'],
            year=self.kwargs['year']
        )
