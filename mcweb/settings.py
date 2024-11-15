"""
Django settings for web-search project.

Generated by 'django-admin startproject' using Django 4.1.dev20220516154624.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import logging
from pathlib import Path
import os

# PyPI
import dj_database_url
import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from django.core.exceptions import ImproperlyConfigured

logger = logging.getLogger(__file__)

# The static version of the app
VERSION = "2.1.0"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

# new config should make this obsolete!
_DEFAULT_ALLOWED_HOSTS = [
    #### production:
    # app.process (mcweb.web) was for rss-fetcher on tarbell
    # now uses https://search.mediacloud.org should now work
    # (need to adjust rss-fetcher config first)
    'search.mediacloud.org', 'mcweb.web',

    #### staging:
    'mcweb-staging.tarbell.mediacloud.org', 'mcweb-staging.steinam.angwin',

    #### development (outside dokku)
    'localhost', '127.0.0.1'
]

# new config should make this obsolete!
_DEFAULT_CSRF_TRUSTED_ORIGINS = [
    'https://mcweb-staging.tarbell.mediacloud.org',
    'https://search.mediacloud.org'
]

# used in defaults below:
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "")

_DEFAULT_ALERTS_RECIPIENTS = []
if ADMIN_EMAIL:
    _DEFAULT_ALERTS_RECIPIENTS.append(ADMIN_EMAIL)

# necessary to run source alerts
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", ADMIN_EMAIL) # user in database

env = environ.Env(      # @@CONFIGURATION@@ definitions (datatype, default value)
    # (cast, default_value) in alphabetical order:
    ALERTS_RECIPIENTS=(list, _DEFAULT_ALERTS_RECIPIENTS),
    ALL_URLS_CSV_EMAIL_MAX=(int, 200000),
    ALL_URLS_CSV_EMAIL_MIN=(int, 25000),
    ALLOWED_HOSTS=(list, _DEFAULT_ALLOWED_HOSTS),
    ANALYTICS_MATOMO_DOMAIN=(str, "null"),
    ANALYTICS_MATOMO_SITE_ID=(str, "null"),
    CACHE_SECONDS=(int, 24*60*60),
    CSRF_TRUSTED_ORIGINS=(list, _DEFAULT_CSRF_TRUSTED_ORIGINS),
    DEBUG=(bool, False),
    EMAIL_BACKEND=(str, 'django.core.mail.backends.smtp.EmailBackend'),
    EMAIL_HOST=(str, ""),
    EMAIL_HOST_PASSWORD=(str, ""),
    EMAIL_HOST_USER=(str, ""),
    EMAIL_HOST_PORT=(int,465),  # ssmtp (SSL submission)
    EMAIL_HOST_USE_SSL=(bool, True),
    EMAIL_NOREPLY=(str, 'noreply@mediacloud.org'),
    EMAIL_ORGANIZATION=(str, "Media Cloud Development"),
    GIT_REV=(str, ""),
    LOG_LEVEL=(str, "DEBUG"),
    NEWS_SEARCH_API_URL=(str, "http://ramos.angwin:8000/v1/"),
    PROVIDERS_TIMEOUT=(int, 60*10),
    REQUEST_LOG_PATH=(str, "/app/requests.log"),
    SCRAPE_ERROR_RECIPIENTS=(list, []),
    SCRAPE_TIMEOUT_SECONDS=(float, 30.0), # http connect/read
    SENTRY_DSN=(str, ""),
    SENTRY_ENV=(str, ""),
    SENTRY_JS_REPLAY_RATE=(float, 0.1), # fraction 0 to 1.0
    SENTRY_JS_TRACES_RATE=(float, 0.2), # fraction 0 to 1.0
    SENTRY_PY_PROFILES_RATE=(float, 1.0), # fraction 0 to 1.0
    SENTRY_PY_TRACES_RATE=(float, 1.0),  # fraction 0 to 1.0
    SYSTEM_ALERT=(str,None),
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# suppress environ package debug messages:
_env_logger = logging.getLogger('environ.environ')
_env_log_level = _env_logger.getEffectiveLevel()
_env_logger.setLevel(logging.INFO)
################ @@CONFIGURATION@@ variables
# (casts and defaults declared above)

# IN ALPHABETICAL ORDER:

ALERTS_RECIPIENTS = env('ALERTS_RECIPIENTS') # list
ALL_URLS_CSV_EMAIL_MAX = env('ALL_URLS_CSV_EMAIL_MAX')
ALL_URLS_CSV_EMAIL_MIN = env('ALL_URLS_CSV_EMAIL_MIN')
ALLOWED_HOSTS = env("ALLOWED_HOSTS") # list
ANALYTICS_MATOMO_DOMAIN = env('ANALYTICS_MATOMO_DOMAIN')
ANALYTICS_MATOMO_SITE_ID = env('ANALYTICS_MATOMO_SITE_ID')

CACHE_SECONDS = env("CACHE_SECONDS")
CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS") # defined as list

DEBUG = env("DEBUG")

EARLIEST_AVAILABLE_DATE = env('EARLIEST_AVAILABLE_DATE') # earliest available date for elastic search

EMAIL_BACKEND = env('EMAIL_BACKEND') # select django.core.mail.backend

# vars used by django.core.mail.backends.smtp.EmailBackend:
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_HOST_PORT = env('EMAIL_HOST_PORT')
EMAIL_HOST_USE_SSL = env('EMAIL_HOST_USE_SSL')

EMAIL_NOREPLY = env('EMAIL_NOREPLY') # email sender address
EMAIL_ORGANIZATION = env('EMAIL_ORGANIZATION') # used in subject line

GIT_REV = env("GIT_REV")      # supplied by Dokku, returned by /api/version
LOG_LEVEL = env('LOG_LEVEL').upper()
NEWS_SEARCH_API_URL = env('NEWS_SEARCH_API_URL')
PROVIDERS_TIMEOUT = env('PROVIDERS_TIMEOUT')

REQUEST_LOG_PATH = env('REQUEST_LOG_PATH')

RSS_FETCHER_URL = env('RSS_FETCHER_URL')
RSS_FETCHER_USER = env('RSS_FETCHER_USER')
RSS_FETCHER_PASS = env('RSS_FETCHER_PASS')

SCRAPE_ERROR_RECIPIENTS = env('SCRAPE_ERROR_RECIPIENTS') # list
SCRAPE_TIMEOUT_SECONDS = env('SCRAPE_TIMEOUT_SECONDS') # HTTP connect/read timeout
SECRET_KEY = env('SECRET_KEY')
SENTRY_DSN = env('SENTRY_DSN')
SENTRY_ENV = env('SENTRY_ENV')
SENTRY_JS_TRACES_RATE = env('SENTRY_JS_TRACES_RATE')
SENTRY_JS_REPLAY_RATE = env('SENTRY_JS_REPLAY_RATE')
SENTRY_PY_PROFILES_RATE = env('SENTRY_PY_PROFILES_RATE')
SENTRY_PY_TRACES_RATE = env('SENTRY_PY_TRACES_RATE')
SYSTEM_ALERT = env('SYSTEM_ALERT')

# end config
_env_logger.setLevel(_env_log_level) # restore log level
#################
# Application definition

INSTALLED_APPS = [
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "frontend",
    "backend.sources",
    "backend.search",
    "backend.users",
    "core",
    "background_task",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "core.logging_middleware.RequestLoggingMiddleware"
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

ROOT_URLCONF = "urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.parse(env('DATABASE_URL'), conn_max_age=0)
}

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 10,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
    {
        "NAME": "backend.users.validators.MinimumAmountOfNumbers",
    },
     {
        "NAME": "backend.users.validators.MinimumAmountOfSpecialCharacters",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = "mcweb/static"

# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],

    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}
# disable nice API browsing in production
if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]


APPEND_SLASH = False

MAX_ATTEMPTS = 1


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'request_file': {  # Custom handler for request logs
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': REQUEST_LOG_PATH,

        },
    },
    'root': {
        'handlers': ['console'],
        'level': LOG_LEVEL,
    },
    'loggers':{
        'request_logger':{
            'handlers':['request_file', 'console'],
            'level':'DEBUG',
            'propagate':False,
        }
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # REDIS_URL supplied by Dokku:
        'LOCATION': env('REDIS_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "cache"
    }
}

DISABLE_SERVER_SIDE_CURSORS = True

#Key: {Value, Type} sets for runtime-configurable app properties. 
#These are editable within the admin console 
CONFIG_DEFAULTS = {
    "request_logging_enabled": {"value": False, "type": bool},
}


################
# since this file is read before logging is configured,
# logging before here is .... unreliable

# this is what happens by default in django.setup() (after loading this file):
logging.config.dictConfig(LOGGING)

try:
    assert EMAIL_HOST, "EMAIL_HOST is empty"
    assert EMAIL_HOST_PASSWORD, "EMAIL_HOST_PASSWORD is empty"
    assert EMAIL_HOST_USER, "EMAIL_HOST_USER is empty"
    logger.info("Email host %s", EMAIL_HOST)
except AssertionError as exc:
    # don't require email settings (for development)
    logger.warning("Email not configured: %s", exc)
    EMAIL_BACKEND = None
    EMAIL_HOST = None
    EMAIL_HOST_USER = None
    EMAIL_HOST_PASSWORD = None
    EMAIL_HOST_PORT = None
    EMAIL_HOST_USE_SSL = None

# sentry config for Python code:
if SENTRY_DSN and SENTRY_ENV:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[
            DjangoIntegration(),
        ],
        environment=SENTRY_ENV,
        traces_sample_rate=SENTRY_PY_TRACES_RATE,
        profiles_sample_rate=SENTRY_PY_PROFILES_RATE,
        release=VERSION,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )
else:
    logger.warning("Sentry not configured")

# add configuration variables above
# (search for @@CONFIGURATION@@ above, in two places)
