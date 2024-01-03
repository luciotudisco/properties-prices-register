#!/bin/sh

echo "Waiting for postgres..."
while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
done
echo "PostgreSQL started"

poetry run python manage.py makemigrations --no-input
poetry run python manage.py migrate --no-input
exec "$@"
