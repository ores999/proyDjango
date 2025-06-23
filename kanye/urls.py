from django.urls import path
from . import views

urlpatterns = [
    path("kanye", views.kanye, name="kanye"),
]