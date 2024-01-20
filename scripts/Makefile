.ONESHELL:

install:
	poetry install --no-root

lint:
	poetry run pre-commit run --all-files

lock:
	poetry lock

reindex:
	poetry run python3 algolia/reindex.py
