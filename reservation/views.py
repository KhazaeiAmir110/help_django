from django.shortcuts import render
from django.views import View
from datetime import date, timedelta

from .models import Company, Category, WorkDate, WorkTime


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
        start_time = date.today()
        end_time = start_time + timedelta(days=30)

        company = Company.objects.get(slug=company_slug)
        work_dates = WorkDate.objects.filter(company=company, date__range=[start_time, end_time])
        return render(request, 'reserve/work_time.html', {'work_dates': work_dates, 'company': company})


# Page 3
class WorkTimeView(View):
    def get(self, request, company_slug, date):
        work_date = WorkDate.objects.get(company__slug=company_slug, date=date)
        work_time = WorkTime.objects.filter(work_date=work_date)
        return render(request, 'reserve/work_hours.html', {'work_time': work_time})
