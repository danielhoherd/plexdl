FROM python:3.8-slim

COPY dist/plexdl*.whl /dist/
RUN pip install --no-cache-dir /dist/plexdl*.whl

ENV PYTHONUNBUFFERED=1
ENV PLEXDL_USER PLEXDL_USER
ENV PLEXDL_PASS PLEXDL_PASS
