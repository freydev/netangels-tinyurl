import os, glob
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)
SECRET_KEY = 'rh()wy0$advm!=_yr%_^n)mupgm8=u9tl2wms*6_v7(tjh!(zx'
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',

    'tinyurl',
    'tinyurl.index',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tinyurl.urls'
WSGI_APPLICATION = 'tinyurl.wsgi.application'
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Asia/Yekaterinburg'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

DEBUG = True
TEMPLATE_DEBUG = True

# import config from settings
config_files_path = os.path.join(PROJECT_DIR, 'settings', '*.conf.py')
config_files = glob.glob(config_files_path)
config_files.sort()

for f in config_files:
    execfile(os.path.abspath(f))

