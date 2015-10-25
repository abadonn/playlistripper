"""
General settings safe to run even with unit tests.
"""
import os

DEBUG = False

TIME_ZONE = "Europe/London"
USE_TZ = True
ADMIN_EMAILS = ('jakub@cubasoft.co.uk', )

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.sqlite3",
        'HOST': "localhost",
        'NAME': "/tmp/playlistripper.db",
    }
}


SECRET_KEY = '5ake7cpr9515sde4otgpmnedso47oq34pokjfhgt93urzpqosr987sje251r87sr'

ALLOWED_HOSTS = ("*", )

INSTALLED_APPS = (
    'django_extensions',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'playlistripper',
    'playlistripper.ripper',
)

ROOT_URLCONF = 'playlistripper.urls'

APPEND_SLASH = True

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)


SESSION_ENGINE = "django.contrib.sessions.backends.file"
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 1209600

_project_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

STATIC_URL = "/static/"
