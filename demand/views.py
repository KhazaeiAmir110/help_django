from django.shortcuts import render, redirect, get_object_or_404
from .models import Demand, Image
from django.views.generic import ListView, DetailView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostEditForm


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
    template_name = 'demand/index.html'
    context_object_name = 'demands'
    model = Demand

    def get_queryset(self):
        return super().get_queryset().filter(category=self.kwargs['category'])


# class EditPostView(LoginRequiredMixin, TemplateView):
#     template_name = 'demand/edit_post.html'
#
#     def get(self, request, slug):
#         demand = Demand.objects.get(slug=slug)
#         form = PostEditForm(instance=demand)
#         return render(request, self.template_name, {'form': form, 'demand': demand})
#
#     def post(self, request, slug):
#         demand = get_object_or_404(Demand, slug=slug)
#         form = PostEditForm(request.user, instance=request.user)
#         if form.is_valid():
#             return redirect('demand:post', slug=slug)
#         return render(request, self.template_name, {'form': form, 'demand': demand})

class EditPostView(UpdateView):
    template_name = 'demand/edit_post.html'
    model = Demand
    # fields = ['title', 'category', 'description', 'short_description', 'image', 'video']
    form_class = PostEditForm
    success_url = '/'
