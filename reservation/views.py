from django.shortcuts import render, get_object_or_404

from django.views import View
from .models import Company, Category


class HomeView(View):
    def get(self, request, category_slug=None):
        companies = Company.objects.all()
        categories = Category.objects.filter(is_subb=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            companies = Company.objects.filter(category=category)
        return render(request, 'home/home.html', {'companies': companies, 'categories': categories})
