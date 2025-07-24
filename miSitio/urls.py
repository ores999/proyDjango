from django.contrib import admin
from django.urls        import path, include
from django.conf        import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views   # 👈

from peliculas import views as peli_views             # 👈

urlpatterns = [
    path('admin/', admin.site.urls),

    # ---------- AUTH ----------
    path('accounts/login/',
         auth_views.LoginView.as_view(
             template_name="registration/login.html"),
         name='login'),

    path('accounts/logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),

    path('accounts/signup/', peli_views.signup, name='signup'),

    # ---------- APPS ----------
    path('evaluacion2', include(('peliculas.urls', 'peliculas'), namespace='peliculas')),
    path('', include('blog.urls')),
    path('', include('kanye.urls')),
    path('accounts/profile/', peli_views.perfil, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)