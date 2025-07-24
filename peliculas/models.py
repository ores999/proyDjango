from django.db import models
from django.utils import timezone
from django.conf import settings

class Pelicula(models.Model):
    titulo        = models.CharField(max_length=200)
    sinopsis      = models.TextField(blank=True)
    fecha_estreno = models.DateField()
    duracion_min  = models.PositiveIntegerField(help_text="Duración en minutos")
    categoria     = models.CharField(max_length=100)           # Acción, Drama…
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="peliculas",
        editable=False,
        null=True, blank=True,
    )

    # ─── NUEVOS CAMPOS DE RATING ─────────────────────────────
    rating_imdb   = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        help_text="Rating IMDb (0-10)",
        blank=True,
        null=True,
    )
    rating_personal = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        help_text="Rating personal (0-5)",
        blank=True,
        null=True,
    )
    # ─────────────────────────────────────────────────────────

    poster        = models.URLField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.titulo} ({self.fecha_estreno.year})"