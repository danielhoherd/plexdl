FROM python:3.8-slim

ADD . /app
WORKDIR /app

RUN pip install . -r requirements.txt

ENV PLEXDL_USER PLEXDL_USER
ENV PLEXDL_PASS PLEXDL_PASS
