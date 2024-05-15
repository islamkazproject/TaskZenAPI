FROM python:3.11.3

LABEL authors="islam"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY src /src
COPY poetry.lock pyproject.toml

RUN pip install --no-cache-dir poetry==1.6.1 \
    && poetry config virtualenvs.create false \
    && poetry install --only main --no-root --no-interaction

RUN adduser --disabled-password --gecos "" admin-user

USER admin-user

WORKDIR /src

EXPOSE 8080
