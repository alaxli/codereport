"""
Django settings for codereport project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# coding=utf-8

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rglwmxr@z@qf@k7z729e*t^%dx_d_jg+o7axoea0s=c21vzmc#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


AUTHENTICATION_BACKENDS = (
    'codereport.auth.backend.LdapBackend',
    'django.contrib.auth.backends.ModelBackend',
)
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'codereport.pagination',
    'svnreport',
    'csreport',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.middleware.transaction.TransactionMiddleware',
    'codereport.middleware.AjaxMiddleware',
    'codereport.middleware.LoginAndPermissionMiddleware',
    'codereport.middleware.ExceptionMiddleware',
    'codereport.pagination.middleware.PaginationMiddleware',
    'django.middleware.locale.LocaleMiddleware',

)

ROOT_URLCONF = 'codereport.urls'

WSGI_APPLICATION = 'codereport.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

ugettext = lambda s:s
LANGUAGES = (
    ('en',ugettext('English')),
    ('zh-cn',ugettext('Chinese')),
)
DEFAULT_CHARSET='utf-8'

USE_I18N = True

USE_L10N = True


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        'svnreport': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

CODEREPORT_ROOT=os.path.dirname(__file__)
TEMPLATE_DIRS = (
    os.path.join(CODEREPORT_ROOT,'..','templates'),
)
LOCALE_PATHS = (
    os.path.join(CODEREPORT_ROOT,'..', 'locale' ),
)

STATIC_ROOT = os.path.join(CODEREPORT_ROOT,'..','static')

STATIC_URL = '/static/'
# Additional locations of static files
STATICFILES_DIRS = (
    ('css',os.path.join(STATIC_ROOT,'css').replace('\\','/') ),
    ('img',os.path.join(STATIC_ROOT,'img').replace('\\','/') ),
    ('js',os.path.join(STATIC_ROOT,'js').replace('\\','/') ),
    ('fonts',os.path.join(STATIC_ROOT,'fonts').replace('\\','/') ),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    )

from internal.settings_local import *
