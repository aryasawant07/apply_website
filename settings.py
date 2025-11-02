from pathlib import Path

# =======================
# Base directory
# =======================
BASE_DIR = Path(__file__).resolve().parent.parent

# =======================
# Security
# =======================
SECRET_KEY = 'django-insecure-change-this-to-your-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# =======================
# Default primary key
# =======================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =======================
# Installed apps
# =======================
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'rest_framework_simplejwt',

    # Custom apps
    'products',
    'users',
    'orders',
]

# =======================
# Middleware
# =======================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =======================
# URL configuration
# =======================
ROOT_URLCONF = 'apple_store_backend.urls'

# =======================
# Templates
# =======================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# =======================
# WSGI
# =======================
WSGI_APPLICATION = 'apple_store_backend.wsgi.application'

# =======================
# Database (SQLite for testing)
# =======================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# =======================
# Password validation
# =======================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =======================
# Internationalization
# =======================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# =======================
# Static files
# =======================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # optional if you have a static folder
STATIC_ROOT = BASE_DIR / 'staticfiles'    # for collectstatic in production

# =======================
# Media files (user-uploaded files)
# =======================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =======================
# REST Framework & JWT
# =======================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# =======================
# Default primary key type
# =======================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
