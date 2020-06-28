FROM frolvlad/alpine-java:jdk8-slim

RUN apk add --no-cache gcc musl-dev
RUN apk add --no-cache g++
RUN apk add python3
RUN apk add go
RUN apk add R
RUN apk add rust
RUN apk add ruby
RUN apk add php-cli
RUN apk add npm
RUN npm install -g underscore shelljs sys lodash async body-parser
RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
    && apk add --update mono@testing  \
    && rm -rf /var/cache/apk/*

