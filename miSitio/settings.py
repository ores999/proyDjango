"""
Django settings for miSitio project.
Generado por 'django-admin startproject' usando Django 3.2.25
"""

from pathlib import Path
from django.urls import reverse_lazy

# ────────────────────────────
# Rutas base
# ────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent


# ────────────────────────────
# Seguridad
# ────────────────────────────
SECRET_KEY = 'django-insecure-!np#3=v**mua+jqnr3=rbvlm_a$wap4)^3@1qwm3t*2csqzgcv'
DEBUG = True           # ponlo en False en producción
ALLOWED_HOSTS = [
    'ores1.pythonanywhere.com',   # dominio PA
    '127.0.0.1',
    'localhost',
]


# ────────────────────────────
# Aplicaciones
# ────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps propias
    'blog',
    'peliculas',
    'kanye'
]


# ────────────────────────────
# Middleware
# ────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ────────────────────────────
# Rutas principales
# ────────────────────────────
ROOT_URLCONF = 'miSitio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],          # usa la detección automática /templates de cada app
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'miSitio.wsgi.application'


# ────────────────────────────
# Base de datos
# ────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ────────────────────────────
# Validación de contraseñas
# ────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {"NAME": 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {"NAME": 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {"NAME": 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ────────────────────────────
# Internacionalización
# ────────────────────────────
LANGUAGE_CODE = 'es-ar'
TIME_ZONE     = 'America/Argentina/Cordoba'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True


# ────────────────────────────
# Archivos estáticos y multimedia
# ────────────────────────────
STATIC_URL = '/static/'

# Carpeta donde *collectstatic* reunirá TODO para producción
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Si NO necesitas rutas adicionales fuera de las apps,
# comenta o elimina STATICFILES_DIRS.  Django ya busca dentro
# de blog/static/, peliculas/static/, etc.
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Media (subidas de usuario: posters, etc.)
MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ────────────────────────────
# Clave primaria por defecto
# ────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGOUT_REDIRECT_URL = reverse_lazy('peliculas:lista_peliculas')
LOGIN_REDIRECT_URL = reverse_lazy('peliculas:lista_peliculas')