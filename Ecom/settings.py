"""
Django settings for Ecom project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i-xg)c4$26ld6)1dy38^mzzex5cap&^57d8j3n8hlbn@1dfc!%'

# SECURITY WARNING: don't run with debug turned on in production!git
DEBUG = False

ALLOWED_HOSTS = ['165.232.177.28','ecom.games']
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'become_admin'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'customer_admin'
LOGOUT_REDIRECT_URL = 'home'
SESSION_COOKIE_AGE=86400
CART_SESSION_ID='cart'


# Application definition

INSTALLED_APPS = [
    
    'customer.apps.CustomerConfig',
    'product.apps.ProductConfig',
    'core.apps.CoreConfig',
    'vendor.apps.VendorConfig',
    'cart.apps.CartConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    


    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'import_export'
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

ROOT_URLCONF = 'Ecom.urls'

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
                'cart.context_processors.cart'
                
                
            ],
        },
    },
]


WSGI_APPLICATION = 'Ecom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
#if DEBUG :
 # DATABASES = {
   # 'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
   # }
 #}
#else:
    

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ecom1db',
        'USER': 'ecom1_admin',
        'PASSWORD': 'testing234',
        'HOST': 'localhost',
        'PORT': '',
    }
}




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS=[
    #BASE_DIR/'static'
#]
STATIC_ROOT = BASE_DIR/'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE':[
            'profile',
            'email',
        ],
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '59475176378-ppme0o63fi6vj3oh2eqjmm5rtf15ag4f.apps.googleusercontent.com',
            'secret': 'sahinc5-m6-r35jQV5Q0nG7n',
            'key': ''
        }
    }
}
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_EMAIL_FROM = 'E-commerce <noreply@django.com>'
SITE_ID=1
LOGIN_REDIRECT_URL='home'
