
"""
Configuración Django de ReforestaSV.
SQL Server en desarrollo y PostgreSQL en Render.
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url


# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


# Identificar si Django se ejecuta en Render
EN_RENDER = os.environ.get("RENDER") == "true"


# Seguridad
SECRET_KEY = os.environ.get("SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError(
        "Falta configurar SECRET_KEY en las variables de entorno."
    )

DEBUG = not EN_RENDER

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

RENDER_EXTERNAL_HOSTNAME = os.environ.get(
    "RENDER_EXTERNAL_HOSTNAME"
)

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Formularios seguros en HTTPS
CSRF_TRUSTED_ORIGINS = []

if RENDER_EXTERNAL_HOSTNAME:
    CSRF_TRUSTED_ORIGINS.append(
        f"https://{RENDER_EXTERNAL_HOSTNAME}"
    )

if EN_RENDER:
    SECURE_PROXY_SSL_HEADER = (
        "HTTP_X_FORWARDED_PROTO",
        "https"
    )
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


# Aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'CampanaReforestacion',
    'Gestion_Arboles',
    'Usuarios',
]


# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'ReforestaSV.urls'


# Plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'ReforestaSV.wsgi.application'


# Bases de datos
if EN_RENDER:
    if not os.environ.get("DATABASE_URL"):
        raise RuntimeError(
            "Falta configurar DATABASE_URL en Render."
        )

    DATABASES = {
        'default': dj_database_url.config(
            env='DATABASE_URL',
            conn_max_age=600,
            conn_health_checks=True,
        )
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'mssql',
            'NAME': os.getenv(
                'DB_NAME', 'reforestasv_bd'
            ),
            'HOST': os.getenv(
                'DB_HOST', 'localhost'
            ),
            'PORT': os.getenv('DB_PORT', ''),
            'USER': os.getenv('DB_USER', ''),
            'PASSWORD': os.getenv('DB_PASSWORD', ''),
            'OPTIONS': {
                'driver': os.getenv(
                    'DB_DRIVER',
                    'ODBC Driver 17 for SQL Server'
                ),
                'trusted_connection': os.getenv(
                    'DB_TRUSTED_CONNECTION', 'yes'
                ),
                'extra_params': (
                    'TrustServerCertificate='
                    + os.getenv(
                        'DB_TRUST_SERVER_CERTIFICATE',
                        'yes'
                    )
                ),
            },
        }
    }


# Validaciones de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Idioma y zona horaria
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    'default': {
        'BACKEND': (
            'django.core.files.storage.FileSystemStorage'
        ),
    },
    'staticfiles': {
        'BACKEND': (
            'whitenoise.storage.CompressedManifestStaticFilesStorage'
        ),
    },
}


# Correo
MAILERS = {
    'default': {
        'BACKEND': (
            'django.core.mail.backends.console.EmailBackend'
        ),
    },
}


# Autenticación
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'