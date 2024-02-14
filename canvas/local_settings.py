from pathlib import Path
import os.path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '!(!iar0(xx=pa-_dnk$di&#^!wqfx5123tur88qgiu_q3h2z6as'

DEBUG = True

ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES = [STATIC_DIR]