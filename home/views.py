from django.views.generic import ListView

from .models import Post


class ListPostView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return super(ListPostView, self).get_queryset().filter(status=Post.StatusEnum.PUBLISHED)
