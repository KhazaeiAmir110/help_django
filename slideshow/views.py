from django.shortcuts import render
from .models import Slideshow


# Create your views here.
def home(request):
    context = {
        'slides': Slideshow.objects.filter(status=True, post__status=True)
    }
    return render(request, 'slideshow.html', context)
