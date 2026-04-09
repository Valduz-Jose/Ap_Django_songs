import os
from pathlib import Path
import environ

# 1. Inicializar environ
env = environ.Env()

# 2. Configuración de rutas (BASE_DIR apunta a la carpeta raíz donde está manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# 3. Forzar lectura del archivo .env
# Usamos os.path.join para asegurar compatibilidad con Windows
env_file = os.path.join(BASE_DIR, '.env')

if os.path.exists(env_file):
    environ.Env.read_env(env_file)
    print(f"✅ Archivo .env cargado exitosamente desde: {env_file}")
else:
    print(f"⚠️ Advertencia: No se encontró el archivo .env en {env_file}")

# 4. Configuración básica (con valores de respaldo para evitar errores de KeyError)

# Seguridad: ¡No dejes esto en True en internet!
DEBUG = env.bool('DEBUG', default=False)
SECRET_KEY = env('SECRET_KEY')

# Quién puede acceder a la app (pon '*' para pruebas, o tu dominio luego)
ALLOWED_HOSTS = ['*']

# 5. Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'canciones', # Nuestra aplicación
]

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

ROOT_URLCONF = 'django_songs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Carpeta de plantillas global
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

WSGI_APPLICATION = 'django_songs.wsgi.application'

# 6. Base de Datos (SQLite temporal para la Fase 1)
# DATABASES = {
#     'default': env.db(), # Esto lee automáticamente la variable DATABASE_URL si existiera
# }
# Pero como definimos variables separadas en el .env, usaremos esta configuración más explícita:
if env('DATABASE_URL', default=None):
    DATABASES = {'default': env.db()}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': env('DB_NAME'),
            'USER': env('DB_USER'),
            'PASSWORD': env('DB_PASSWORD'),
            'HOST': env('DB_HOST'),
            'PORT': env('DB_PORT'),
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }

# 7. Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 8. Internacionalización
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 9. Archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # Directorio donde se reunirán en producción

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'