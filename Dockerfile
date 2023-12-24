FROM --platform=linux/amd64 ubuntu:latest

RUN apt-get update && apt-get install -y \
    clang \
    make

WORKDIR /app