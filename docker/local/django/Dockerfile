# Pull Image

ARG PYTHON_VERSION=latest

FROM python:${PYTHON_VERSION} as python

ENV BUILD_ENVIRONMENT=local
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY /requirements/* /app/requirements/

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3-pip \
    && pip install --upgrade pip setuptools wheel

RUN pip install -r requirements/${BUILD_ENVIRONMENT}.txt

COPY . /app/