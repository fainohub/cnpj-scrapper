FROM python:3.8-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN pip install mysql-connector-python

COPY ./src /app/

WORKDIR /app