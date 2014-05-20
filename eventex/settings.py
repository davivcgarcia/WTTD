"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

AUTHOR: Davi Garcia (davivcgarcia@gmail.com)
DATE: 05/20/2014
"""

# Project Imports.

import dj_database_url
from unipath import Path

# General Configuration.

BASE_DIR = Path(__file__).parent
SECRET_KEY = '8y)@(krme@28r2e3j5=irunc8(+8)fxqbevlg%1xmkov%6$6=='
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

# Application definition.

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'eventex.core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'eventex.urls'

WSGI_APPLICATION = 'eventex.wsgi.application'


# Database using dj-database-url for Heroku and Unipath.

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite3:///' + BASE_DIR.child('db.sqlite3')
    )
}

# Internationalization.

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static Files to be served by Django with dj-static.

STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'
