FROM python:3.14

RUN apt-get update && \
    apt-get install -y git \
                       gcc \
                       libffi-dev \
                       default-libmysqlclient-dev \
                       nodejs \
                       libffi-dev

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN apt-get install -y npm

RUN npm install -g bower less