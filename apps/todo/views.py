from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import TodoList, TodoItem
from .forms import TodoListForm, TodoItemForm


@login_required
def lists(request):
    form = TodoListForm()
    todo_list = TodoList.objects.filter(user=request.user)

    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            new_list = TodoList(title=title, user=request.user)
            new_list.save()
            form = TodoListForm()

    return render(request, 'list.html', {'list': todo_list, 'form': form})


@login_required
def list_detail(request, id):
    form = TodoItemForm()
    selected_list = TodoList.objects.get(id=id)
    items = selected_list.items.all()

    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            new_item = TodoItem(title=title, description=description, todo_list=selected_list)
            new_item.save()
            form = TodoItemForm()

    context = {
        'items': items,
        'selected_list': selected_list,
        'form': form
    }
    return render(request, 'detail.html', context)


def delete_list(request, id):
    selected_list = TodoList.objects.get(id=id)
    if request.method == 'POST':
        selected_list.delete()
        return redirect('todo-list')


def delete_item(request, id):
    selected_list = TodoItem.objects.get(id=id)
    if request.method == 'POST':
        selected_list.delete()
        return redirect('detail')
