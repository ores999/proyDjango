# Generated by Django 3.2.25 on 2025-06-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='rating_imdb',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='Rating IMDb (0-10)', max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='rating_personal',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='Rating personal (0-5)', max_digits=2, null=True),
        ),
    ]
