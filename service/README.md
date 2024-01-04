# Setup & running locally

To start the container, run:

```shell
make runserver
```

## Run tests

Run descriptive tests in the container using:

```shell
docker exec -it <container_name> poetry run pytest -rP -vv
```
