FROM python:3.7-slim-stretch

WORKDIR /opt/api

COPY requirements.txt /requirements.txt
RUN pip install -U pip; pip install -r /requirements.txt \
    && python3 -m pip install redis

COPY . .