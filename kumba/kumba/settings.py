"""
Django settings for kumba project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')q@gc3hylqq)ey7r3g2+txid1*5@j2-)e9jh%1t&69wga$97ff'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'scenetext',
    'corsheaders',
    'djcelery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kumba.urls'

WSGI_APPLICATION = 'kumba.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
TEMPLATE_DIRS = (
		os.path.join(BASE_DIR,'templates'),
		)
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = ()

CORS_ORIGIN_REGEX_WHITELIST = ()

CORS_URLS_REGEX = '^.*$'

CORS_ALLOW_METHODS = (
		    'GET',
			        'POST',
				        'PUT',
					        'PATCH',
						        'DELETE',
							        'OPTIONS'
								    )

CORS_ALLOW_HEADERS = (
		        'x-requested-with',
			        'content-type',
				        'accept',
					        'origin',
						        'authorization',
							        'x-csrftoken'
								    )

CORS_EXPOSE_HEADERS = ()

CORS_PREFLIGHT_MAX_AGE = 86400

CORS_ALLOW_CREDENTIALS = True

CORS_REPLACE_HTTPS_REFERER = True
