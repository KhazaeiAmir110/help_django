from django.shortcuts import render
from django.views import View

from .models import Company, Category, WorkDate


class HomeView(View):
    def get(self, request, category_slug=None):
        companies = Company.objects.all()
        categories = Category.objects.filter(is_subb=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            companies = Company.objects.filter(category=category)
        return render(request, 'home/home.html', {'companies': companies, 'categories': categories})


# Page 2

class WorkDateView(View):
    def get(self, request, company_slug):
        company = Company.objects.get(slug=company_slug)
        work_dates = WorkDate.objects.filter(company=company)
        return render(request, 'reserve/work_time.html', {'work_dates': work_dates, 'company': company})
