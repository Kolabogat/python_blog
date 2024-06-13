#!/bin/sh

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py command_create_categories
python manage.py command_create_difficulties
DJANGO_SUPERUSER_USERNAME=$DJANGO_SUPERUSER_USERNAME DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD python manage.py createsuperuser --noinput --email $DJANGO_SUPERUSER_EMAIL
python manage.py optional_command_create_articles

gunicorn backend.wsgi:application --bind 0.0.0.0:8000
