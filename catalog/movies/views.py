from django.shortcuts import render
from .models import Movies
from django.shortcuts import get_object_or_404
#from django.http import Http404

# Create your views here.



def index(request):
    movies = Movies.objects.all()
    context = {
        "movies": movies,
    }
    return render(request, "movies/index.html", context)

def details(request, movie_id):
    """
        try:
            movie = Movies.objects.get(pk=movie_id)
        except Movies.DoesNotExist:
            raise Http404("No Movies")
    """

    movie = get_object_or_404(Movies,pk=movie_id)
    context = {
        "movie": movie,
    }
    return render(request, "movies/details.html", context)

def search(request):
    return render(request, "movies/search.html")