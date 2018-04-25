"""
Django settings for tkprj project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from .settings_secret import secret_vars

"""
 The file settings_secret contains a dict secret_vars with all senssible information 
 used on settings file
 of course it is not on github repository
 Example of settings_secret.py content : 

secret_vars = {
 'EMAIL_HOST':'mail.yourdomain.com',
 'EMAIL_PORT':25,
 'EMAIL_HOST_USER':'user@yourdomain.com',
 'EMAIL_HOST_PASSWORD':'***********',
 'EMAIL_USE_TLS':True,
 'DEFAULT_FROM_EMAIL':'suportuser@yourdomain.com',
 'SECRET_KEY':'*****************************************',
}
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Use the following  command to generate your secret key
#
# python manage.py generate_secret_key [--replace] [secretkey.txt]
#
# and use this to keep it secret 
#
# with open('/path/to/the/secretkey.txt') as f:
#    SECRET_KEY = f.read().strip()

SECRET_KEY = secret_vars["SECRET_KEY"] 
EMAIL_HOST = secret_vars["EMAIL_HOST"]
EMAIL_HOST = secret_vars["EMAIL_HOST"] 
EMAIL_PORT = secret_vars["EMAIL_PORT"] 
EMAIL_HOST_USER = secret_vars["EMAIL_HOST_USER"] 
EMAIL_HOST_PASSWORD = secret_vars["EMAIL_HOST_PASSWORD"] 
EMAIL_USE_TLS = secret_vars["EMAIL_USE_TLS"] 


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
   'tickets.qvaliz.pt',
   'localhost',
]


FIXTURE_DIRS = ['initial_data']

LOCALE_PATHS = (
    '~/git-repos/tkprj/tickets/locale', )


# Application definition

INSTALLED_APPS = [
    'tickets.apps.TicketsConfig',
    'bootstrap3',
    'bootstrap', 
    'fontawesome',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'tkprj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'tkprj.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# include 'PASSWORD' if you are not using an ident server
# change user name and database configurations as needed
# The initial database must contain an schema tickets

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tkprj',
        'HOST': '127.0.0.1',
        'USER': 'marcotc', 
	'PORT': '5432',	
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	'OPTIONS': {
		'min_length': 5,
	}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'pt'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

#PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
#STATIC_ROOT = os.path.join(PROJECT_DIR, 'tickets/static') 
STATIC_URL = '/static/'

DEFAULT_FROM_EMAIL = secret_vars["DEFAULT_FROM_EMAIL"]

BOOTSTRAP3 = {

    # The URL to the jQuery JavaScript file
    'jquery_url': '//code.jquery.com/jquery.min.js',

    # The Bootstrap base URL
    'base_url': '//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/',

    # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    'css_url': None,

    # The complete URL to the Bootstrap CSS file (None means no theme)
    'theme_url': None,

    # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
    'javascript_url': None,

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
    'javascript_in_head': True,

    # Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
    'include_jquery': True,

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-3',

    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-9',

    # Set HTML required attribute on required fields, for Django <= 1.8 only
    'set_required': True,

    # Set HTML disabled attribute on disabled fields, for Django <= 1.8 only
    'set_disabled': False,

    # Set placeholder attributes to label if no placeholder is provided.
    # This also considers the 'label' option of {% bootstrap_field %} tags.
    'set_placeholder': True,

    # Class to indicate required (better to set this in your Django form)
    'required_css_class': '',

    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'has-error',

    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    'success_css_class': 'has-success',

    # Renderers (only set these if you have studied the source and understand the inner workings)
    'formset_renderers':{
        'default': 'bootstrap3.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap3.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}
