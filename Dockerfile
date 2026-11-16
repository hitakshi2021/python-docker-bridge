FROM python:3.11-slim

WORKDIR /app

COPY writer.py . 
COPY reader.py .

RUN mkdir /shared_data