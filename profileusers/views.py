from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from users.models import User


class ProfileUserView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        # context['demands'] = Demand.objects.filter(user=self.request.user)
        # context['form'] = DemandForm()
        return context

    # def post(self, request, *args, **kwargs):
    #     form = DemandForm(request.POST)
    #     if form.is_valid():
    #         demand = form.save(commit=False)
    #         demand.user = request.user
    #         demand.save()
    #     return self.get(request, *args, **kwargs)
