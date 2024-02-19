"""
Django settings for simple_signup project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ctu&l@#*2o+dh5nb25=zl1iv*^=c#43yiy-t7*kc6tlv-m-&)p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []  # ['127.0.0.1'] по умолчанию


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',

    # apps необходимые для allauth
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'sign',  # приложение регистрации, аутентификации и авторизации
    'protect',  # приложение "декоратор" для проверки аутентификации

    # apps allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... регистрация посредством провайдера:
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # настройки middleware для allauth
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'simple_signup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # путь к шаблонам
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                # `allauth` needs this from django
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# URL-адрес страницы аутентификации
LOGIN_URL = '/accounts/login/'  # теперь логин через allauth.account
# редирект после успешного входа на сайт
LOGIN_REDIRECT_URL = '/'

# используется в случае, если данный проект управляет несколькими сайтами
SITE_ID = 1

# бэкенды аутентификации [для allauth]
AUTHENTICATION_BACKENDS = [
    # встроенный бэкенд Django, реализующий аутентификацию по username
    'django.contrib.auth.backends.ModelBackend',
    # бэкенд аутентификации, предоставленный пакетом allauth
    # : по email или сервис-провайдеру
    'allauth.account.auth_backends.AuthenticationBackend',
]

# настройки allauth для входа/регистрации по email
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
# username не требуется
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# подтверждение почты отключено
ACCOUNT_EMAIL_VERIFICATION = 'none'
# замена стандартной формы регистрации кастомной
ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

WSGI_APPLICATION = 'simple_signup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
