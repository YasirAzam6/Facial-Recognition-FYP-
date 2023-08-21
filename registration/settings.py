import os
import pymongo
from django.contrib.auth import get_user_model


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Generate a new secret key
SECRET_KEY = os.urandom(32).hex()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'app1',
    'django.contrib.staticfiles',
    'mongoengine',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


ROOT_URLCONF = 'registration.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'registration.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'new',
        'HOST': 'localhost',
        'PORT': 27017,
        'AUTH_SOURCE': 'admin',
        # 'USERNAME': 'your-username',
        # 'PASSWORD': 'your-password',
        'ENFORCE_SCHEMA': False,  # Set this to True if you want to enforce schema validation
    }
}
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['new']

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# EMAIL
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'yasirrana818@gmail.com'
# EMAIL_HOST_PASSWORD = 'aqxouhbzfqflxoxg'  # Replace with your application-specific password
# EMAIL_USE_TLS = True  # or False if your email server doesn't require TLS


# settings.py Uni Try

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # e.g., 'smtp.gmail.com'
EMAIL_PORT = 587  # Use the appropriate port for your email host
EMAIL_HOST_USER = 'yasirrana818@gmail.com'  # Sender email address
EMAIL_HOST_PASSWORD = 'aqxouhbzfqflxoxg'  # Sender email password
EMAIL_USE_TLS = True  # Use TLS encryption for secure connection






# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
# MEDIA_URL = '/uploads/'

# Add the new secret key to the settings
SECRET_KEY = '<your-new-secret-key>'

# SESSION_ENGINE = 'mongoengine.django.sessions'
