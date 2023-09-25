from .models import Demand, Category
from django.views.generic import DetailView, TemplateView, UpdateView
from .forms import PostEditForm


# Create your views here.


class Home(TemplateView):
    template_name = 'demand/index.html'
    context_object_name = 'demands'
    queryset = Demand.objects.filter(status='p')


class Post(DetailView):
    template_name = 'demand/post.html'
    context_object_name = 'demands'
    model = Demand

    def get_queryset(self):
        return super().get_queryset().filter(slug=self.kwargs['slug'])


class CategoryPageView(DetailView):
    template_name = 'demand/category.html'
    context_object_name = 'demands'
    model = Category

    def get_queryset(self):
        category = self.kwargs['slug']
        return super().get_queryset().filter(slug=category)


class EditPostView(UpdateView):
    template_name = 'demand/edit_post.html'
    model = Demand
    # fields = ['title', 'category', 'description', 'short_description', 'image', 'video']
    form_class = PostEditForm
    success_url = '/'
