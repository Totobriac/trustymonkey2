"""
Django settings for trusty_monkey project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-jc7uv=+k#uv&ww&9^z@(!=49#rn7bxipp%2uagwjvcdkc&u19'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["trustymonkey2.herokuapp.com", "127.0.0.1"]
# ALLOWED_HOSTS = ["127.0.0.1"]


from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = default_headers + (
    'Access-Control-Allow-Origin',
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'storages',
    
    'places',
    'users',
    'rest_framework',
    'rest_framework.authtoken',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'crispy_forms',    
    'drf_multiple_model',
    'webpack_loader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'trusty_monkey.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'trusty_monkey.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# postgres://tqtgbxapqgliyd:81cfbc9ba60e50d18b800b7347f380799b56b4e767c170e15be8090ee8e14dd8@ec2-54-75-244-161.eu-west-1.compute.amazonaws.com:5432/d22v942f7oedqh

# this url follow this pattern
# postgres://user:pass@host:port/name

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'dd66tpiie8rprf',
#         'USER': 'gdlrkeljglkyqu',
#         'PASSWORD': 'acedceb3813a345947e3225c1e7493e988d41dc5ecc193ba48eb15679267c441',
#         'HOST': 'ec2-54-166-251-173.compute-1.amazonaws.com',
#         'PORT': '5432'
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd751emj1l26su7',
#         'USER': 'ogfvybcmsvalua',
#         'PASSWORD': '5bc91c850bbda7e2a15a9699f6afdd17531f544d0c2805726d12a1b230cf9a0e',
#         'HOST': 'ec2-46-137-124-19.eu-west-1.compute.amazonaws.com',
#         'PORT': '5432'
#     }
# }
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
if 'test' in sys.argv:
    #Configuration for test database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'd613uir5h19hl',
            'USER': 'wbyiomoeypyywj',
            'PASSWORD': 'f26e1b630963d5305fef8bc4a17680ee866667297357aca0e412f06891aed646',
            'HOST': 'ec2-46-137-124-19.eu-west-1.compute.amazonaws.com',
            'PORT': 5432,
            'TEST': {
                'NAME': 'd613uir5h19hl', #This is an important entry
            }
        }
    }
else:
  #Default configuration
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'd751emj1l26su7',
            'USER': 'ogfvybcmsvalua',
            'PASSWORD': '5bc91c850bbda7e2a15a9699f6afdd17531f544d0c2805726d12a1b230cf9a0e',
            'HOST': 'ec2-46-137-124-19.eu-west-1.compute.amazonaws.com',
            'PORT': 5432,
            'TEST': {
                'NAME': 'd751emj1l26su7',
            }
        }
    }

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/src/assets"),
    os.path.join(BASE_DIR, "frontend/dist")
]

MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'uploaded_media')
# MEDIA_URL = os.path.join(BASE_DIR, '..', 'media/')
MEDIA_URL = '/media/'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),    
}


CRISPY_TEMPLATE_PACK = "bootstrap4"
LOGIN_URL ="accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# AWS S3 SETUP BEGIN
AWS_ACCESS_KEY_ID = 'AKIAYHDIXNIEF2EVK65Y'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'trustymonkey'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_REGION_NAME = "eu-west-3"
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS S3 SETUP END

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = (True)

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend', 'webpack-stats.json'),
    }
}

SECURE_SSL_REDIRECT = False

APPEND_SLASH = False
