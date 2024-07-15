from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import TodoList


@login_required
def lists(request):
    todo_list = TodoList.objects.filter(user=request.user)
    return render(request, 'list.html', {'list': todo_list})


@login_required
def list_detail(request, id):
    selected_list = TodoList.objects.get(id=id)
    items = selected_list.items.all()

    context = {
        'items': items,
        'selected_list': selected_list,
    }
    return render(request, 'detail.html', context)
