from django.shortcuts import render
from .models import Publicacion
from django.utils import timezone
from django.contrib.auth.models import User

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    return render(request, 'blog/lista_publicaciones.html', {'publicaciones': publicaciones})

    