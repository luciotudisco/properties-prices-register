# Pull official base image
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory
WORKDIR /app

# Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYCURL_SSL_LIBRARY=openssl

RUN apt-get update \
    && apt-get install -y gcc gunicorn python3-dev musl-dev libmagic1 libffi-dev netcat-traditional \
    build-essential libpq-dev libcurl4-openssl-dev libssl-dev

COPY poetry.lock pyproject.toml /app/
RUN pip3 install poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . /app/

ENTRYPOINT [ "/entrypoint.sh" ]
