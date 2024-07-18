from django.urls import path

from .views import lists, list_detail, delete_list, delete_item, send

urlpatterns = [
    path('b/', lists, name='todo-list'),
    path('<int:id>/', list_detail, name='detail'),
    path('delete_list/<int:id>/', delete_list, name='delete_list'),
    path('delete_item/<int:id>', delete_item, name='delete_item'),
    path('send/', send, name='send'),
]
