from django.urls import path
from .views import Home, QuestionView

app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('questions/', QuestionView.as_view(), name='question'),
    path('questions/<int:pk>/', QuestionView.as_view()),
]

# چون برای put نیاز به pk است به همین دلیل باید یک url جدید برای آن تعریف کنیم
