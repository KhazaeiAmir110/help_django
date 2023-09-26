from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from demand.models import Demand, Image, Video
from .forms import DemandForm, UserProfileEditForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['demands'] = Demand.objects.filter(user=self.request.user)
        context['form'] = DemandForm()
        return context

    def post(self, request, *args, **kwargs):
        form = DemandForm(request.POST)
        if form.is_valid():
            demand = form.save(commit=False)
            demand.user = request.user
            demand.save()
        return self.get(request, *args, **kwargs)


class CreateDemandView(View):
    def get(self, request):
        form = DemandForm()
        context = {'form': form}
        return render(request, 'registration/create_demand.html', context)

    def post(self, request):
        form = DemandForm(request.POST, request.FILES)
        image_file = request.POST.get('image')
        video_file = request.POST.get('video')
        if image_file:
            image = Image(file=image_file)
            image.save()
        if video_file:
            video = Video(file=video_file)
            video.save()
        if form.is_valid():
            demand = form.save(commit=False)
            demand.user = request.user
            demand.image = image
            demand.video = video
            demand.save()
            return redirect(
                'users:profile')  # یا هر مسیری که بعد از ذخیره کردن مطلبه جدید به آن هدایت می‌شود

        context = {'form': form}
        return render(request, 'registration/create_demand.html', context)


class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/edit_profile.html'

    def get(self, request):
        form = UserProfileEditForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
        return render(request, self.template_name, {'form': form})


class ProfileHomeView(TemplateView):
    template_name = 'registration/home.html'
