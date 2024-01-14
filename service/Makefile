.ONESHELL:

install:
	poetry install --no-root

runserver: install
	docker compose -f docker-compose.dev.yaml build && docker compose -f docker-compose.dev.yaml up

lint:
	poetry run pre-commit run --all-files

lock:
	poetry lock

test: install
	docker-compose -f docker-compose.dev.yaml run --rm api python manage.py test --pattern="test_*.py" --verbosity=2
