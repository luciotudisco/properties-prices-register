.ONESHELL:

runserver:
	poetry run python manage.py runserver

lint:
	poetry run pre-commit run --all-files

lock:
	poetry lock
