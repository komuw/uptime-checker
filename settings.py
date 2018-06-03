import os


def here(*args):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *args)


PROJECT_ROOT = here('')


def project_root_joiner(*args):
    return os.path.join(os.path.abspath(PROJECT_ROOT), *args)


ALLOWED_HOSTS = '*'
SECRET_KEY = 'A-random-and-secure-secret-key'
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
STATIC_ROOT = project_root_joiner('', 'static/')
STATIC_URL = '/static/'
