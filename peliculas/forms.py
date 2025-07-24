from django import forms
from .models import Pelicula


class PeliculaForm(forms.ModelForm):
    """Formulario para crear / editar películas; el campo autor se
    completa en la vista → no aparece aquí."""
    
    class Meta:
        model  = Pelicula
        
        exclude = ["autor", "fecha_creacion"]

        widgets = {
            "titulo":        forms.TextInput(attrs={"class": "input"}),
            "sinopsis":      forms.Textarea(attrs={"rows": 5}),
            "fecha_estreno": forms.DateInput(attrs={"type": "date"}),
            "duracion_min":  forms.NumberInput(attrs={"min": 1}),
            "categoria":     forms.TextInput(),
            "rating_imdb":   forms.NumberInput(attrs={"step": "0.1", "min": 0, "max": 10}),
            "rating_personal": forms.NumberInput(attrs={"step": "0.5", "min": 0, "max": 5}),
        }