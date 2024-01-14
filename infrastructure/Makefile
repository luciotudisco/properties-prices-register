.ONESHELL:

install:
	npm install -g aws-cdk
	poetry install

test: install
	poetry run pytest tests

deploy: install
	cdk deploy --all --require-approval=never

lint:
	poetry run pre-commit run --all-files

lock:
	poetry lock
