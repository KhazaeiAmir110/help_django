from django.urls import path
from .views import Home, QuestionListView, QuestionCreatViews, QuestionDeleteViews, \
    QuestionUpdateViews

app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('questions/', QuestionListView.as_view(), name='question'),
    path('question/<int:pk>/', QuestionUpdateViews.as_view(), name='list-questions'),
    path('question/ceate/', QuestionCreatViews.as_view(), name='creat-question'),
    path('question/delete/', QuestionDeleteViews.as_view(), name='delete-question'),
]
