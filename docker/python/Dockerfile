FROM python:3.7-alpine3.12

RUN mkdir /script && \
    apk update;\
    apk add --no-cache bash; \
    rm -rf /var/cache/apk/*
COPY ./script /script
