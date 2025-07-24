from django.contrib import admin
from .models import Pelicula

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha_estreno", "autor")
    search_fields = ("titulo", "categoria")
    list_filter = ("categoria",)