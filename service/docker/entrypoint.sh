#!/bin/sh
poetry run python manage.py makemigrations --no-input
poetry run python manage.py migrate --no-input
exec "$@"
