from django.shortcuts import render
from movies.models import Movies

# Create your views here.


def index(request):
    movies = Movies.objects.filter(isHome=True, isPublished= True)
    context = {
        "movies": movies,
    }
    return render(request, "pages/index.html", context)


def about(request):
    return render(request, "pages/about.html")