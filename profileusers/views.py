from django.views.generic import TemplateView
from django.shortcuts import render

from .mixins import ProfileUserViewMixin


class HomeProfileView(ProfileUserViewMixin, TemplateView):
    template_name = 'dashboard/index.html'
