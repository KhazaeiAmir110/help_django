from django.shortcuts import render
from .models import Demand, Image
from django.views.generic import ListView, DetailView, TemplateView


# Create your views here.


class Home(ListView):
    template_name = 'demand/index.html'
    context_object_name = 'demands'
    queryset = Demand.objects.filter(status='p')


# def post(request, slug):
#     context = {
#         'demand': Demand.objects.get(slug=slug)
#     }
#     return render(request, 'demand/post.html', context=context)


class Post(DetailView):
    template_name = 'demand/post.html'
    context_object_name = 'demands'
    model = Demand

    def get_queryset(self):
        return super().get_queryset().filter(slug=self.kwargs['slug'])


class Form(TemplateView):
    template_name = 'demand/contact.html'
