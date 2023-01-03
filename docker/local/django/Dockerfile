# Pull Image

ARG PYTHON_VERSION=latest

FROM python:${PYTHON_VERSION} as python

ENV BUILD_ENVIRONMENT=local
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY /requirements/* /app/requirements/

RUN pip install -r requirements/${BUILD_ENVIRONMENT}.txt

COPY . /app/

EXPOSE 8000

COPY ./docker/local/django/start /start
RUN chmod +x /start

CMD [ "/start" ]