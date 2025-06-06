from django.shortcuts import render
from .models import Pelicula

def lista_peliculas(request):
    peliculas = Pelicula.objects.order_by('-fecha_estreno')
    return render(request, "peliculas/lista_peliculas.html",
                  {"peliculas": peliculas})