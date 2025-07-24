from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import PeliculaForm
from .models import Pelicula


# ───────────────────────────────────────────────
# Lista de películas
# ───────────────────────────────────────────────
def lista_peliculas(request):
    """Página principal: muestra las películas ordenadas por fecha de estreno."""
    peliculas = Pelicula.objects.order_by("-fecha_estreno")
    return render(
        request,
        "peliculas/lista_peliculas.html",
        {"peliculas": peliculas},
    )


# ───────────────────────────────────────────────
# Registro de usuarios
# ───────────────────────────────────────────────
def signup(request):
    """Formulario de registro de nuevos usuarios."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Cuenta creada, inicia sesión!")
            return redirect("login")        # nombre de ruta del auth
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


# ───────────────────────────────────────────────
# Crear nueva película
# ───────────────────────────────────────────────
@login_required
def crear_pelicula(request):
    """Crea una película asociada al usuario autenticado."""
    if request.method == "POST":
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            peli = form.save(commit=False)
            peli.autor = request.user
            peli.save()
            messages.success(request, "¡Película creada!")
            return redirect("peliculas:lista_peliculas")
    else:
        form = PeliculaForm()
    return render(request, "peliculas/crear_pelicula.html", {"form": form})


@login_required
def perfil(request):
    # Aquí simplemente mostramos las pelis del usuario, por ejemplo
    mis_pelis = Pelicula.objects.filter(autor=request.user)
    return render(request, "peliculas/perfil.html",
                  {"mis_pelis": mis_pelis})