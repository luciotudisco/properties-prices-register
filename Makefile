.ONESHELL:

runserver:
	docker compose -f docker-compose.dev.yaml build && docker compose -f docker-compose.dev.yaml up

lint:
	poetry run pre-commit run --all-files

lock:
	poetry lock
