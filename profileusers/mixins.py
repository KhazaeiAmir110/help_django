from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import User
from home.models import Post, Category, File


class ProfileUserViewMixin(LoginRequiredMixin):

    def __init__(self):
        self.request = None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_superuser:
            context = {
                'user': user,
                'users': User.objects.all(),
                'posts': Post.objects.all(),
                'categories': Category.objects.all(),
                'files': File.objects.all()
            }
        elif user.is_active:
            context = {
                'user': user,
                'post': Post.objects.filter(user=self.request.user)
            }
        else:
            context = {
                'error': 'You are not authorized to access this!!!'
            }

        return context

    def post(self, request, *args, **kwargs):
        # form = form(request.POST)
        form = ''
        if form.is_valid():
            demand = form.save(commit=False)
            demand.user = request.user
            demand.save()
        return self.get(request, *args, **kwargs)
