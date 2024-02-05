from django.views.generic import ListView, DetailView

from .models import Post


class ListPostView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return super(ListPostView, self).get_queryset().filter(status=Post.StatusEnum.PUBLISHED)


class PostDetailView(DetailView):
    model = Post
    template_name = "single.html"
    context_object_name = 'post'

    def get_queryset(self):
        return super().get_queryset().filter(title=self.kwargs['title'])
