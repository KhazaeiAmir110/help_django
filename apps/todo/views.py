from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import TodoList


@login_required
def list_detail(request):
    todo_list = TodoList.objects.filter(user=request.user)
    return render(request, 'list.html', {'list': todo_list})
