from django.urls import path
from . import views

app_name = "peliculas"           # evita confusiones con otros names

urlpatterns = [
    path('',              views.lista_peliculas, name='lista_peliculas'),
    path('nueva/',        views.crear_pelicula,  name='crear_pelicula'),
]