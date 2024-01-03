.ONESHELL:

runserver:
	docker compose build && docker compose up

lint:
	poetry run pre-commit run --all-files

lock:
	poetry lock
