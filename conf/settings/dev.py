from .common import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# override secret
SECRET_KEY = "akr2icmg1n8%z^3fe3c+)5d0(t^cy-2_25rrl35a7@!scna^1#"

# override common debug setting
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'tmp', 'db.sqlite3'),
        'USER': 'democracy',
        'PASSWORD': 'democracy',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'src/django/static'),
]

# Override app settings
REACT['RENDER'] = DEBUG

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/local/',  # end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'conf', 'webpack', 'webpack-stats-local.json'),
    }
}
